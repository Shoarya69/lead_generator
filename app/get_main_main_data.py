import asyncio
import json
import re
from playwright.async_api import async_playwright

# URLS = [
#     "YOUR_URL_1",
#     "YOUR_URL_2",
#     # add 100 urls
# ]

# CONCURRENT_PAGES = 10


def extract_data(text):

    result = {}

    # PHONE
    phone = re.findall(r'tel:\+?[0-9]+', text)

    if phone:
        result["phone"] = phone[0].replace("tel:", "")

    # WEBSITE
    websites = re.findall(r'https://[^"]+', text)

    clean_sites = []

    for w in websites:

        if (
            "google" not in w
            and "gstatic" not in w
            and "googleusercontent" not in w
        ):
            clean_sites.append(w)

    if clean_sites:
        result["website"] = clean_sites[0]

    # RATING
    rating = re.findall(
        r'\[null,null,null,null,null,null,null,([0-9.]+)\]',
        text
    )

    if rating:
        result["rating"] = rating[0]

    # NAME
    # name = re.findall(r'"([^"]+)"\,null\,\["Gym"', text)

    # if name:
    #     result["name"] = name[0]

    return result


async def process_url(context, lead, semaphore):

    async with semaphore:

        page = await context.new_page()
        url=lead[1]
        id=lead[0]
        final_data = {
            "id": id,
            "url": url
        }

        try:

            async def handle_response(response):

                nonlocal final_data

                if "/maps/preview/place" not in response.url:
                    return

                try:

                    body = await response.text()

                    data = extract_data(body)

                    if data:
                        final_data.update(data)

                except:
                    pass

            page.on("response", handle_response)

            await page.goto(
                url,
                wait_until="domcontentloaded",
                timeout=30000
            )

            # WAIT ONLY UNTIL DATA COMES
            for _ in range(20):

                if "phone" in final_data:
                    break

                await asyncio.sleep(0.2)

        except Exception as e:

            final_data["error"] = str(e)

        await page.close()

        return final_data


async def main(CONCURRENT_PAGES, URLS):

    semaphore = asyncio.Semaphore(CONCURRENT_PAGES)

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True,
            args=[
                "--disable-blink-features=AutomationControlled"
            ]
        )

        context = await browser.new_context()

        # BLOCK HEAVY FILES
        async def block_resources(route):

            if route.request.resource_type in [
                "image",
                "font",
                "media",
                "stylesheet"
            ]:
                await route.abort()

            else:
                await route.continue_()

        await context.route("**/*", block_resources)

        tasks = []

        for url in URLS:

            tasks.append(
                process_url(
                    context=context,
                    lead=url,
                    semaphore=semaphore
                )
            )

        results = await asyncio.gather(*tasks)

        print(json.dumps(results, indent=4))
        await browser.close()
        return results

if __name__ == "__main__":
    asyncio.run(main())