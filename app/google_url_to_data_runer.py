import asyncio
import json
import re
from playwright.async_api import async_playwright

URL = "https://www.google.com/maps/place/Zone+Gym/@51.5946481,-0.1129059,17z/data=!3m1!4b1!4m6!3m5!1s0x48761be146572445:0x2d37acbbea14b2ad!8m2!3d51.5946481!4d-0.1129059!16s%2Fg%2F1yh9tz67v?authuser=0&hl=en&entry=ttu&g_ep=EgoyMDI2MDUwMi4wIKXMDSoASAFQAw%3D%3D"


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
    rating = re.findall(r'\[null,null,null,null,null,null,null,([0-9.]+)\]', text)

    if rating:
        result["rating"] = rating[0]

    # NAME
    name = re.findall(r'"([^"]+)"\,null\,\["Gym"', text)

    if name:
        result["name"] = name[0]

    return result


async def main():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=True
        )

        page = await browser.new_page()

        final_data = {}

        async def handle_response(response):

            nonlocal final_data

            url = response.url

            if "/maps/preview/place" not in url:
                return

            try:

                body = await response.text()

                data = extract_data(body)

                if data:
                    final_data = data

            except Exception as e:
                print(e)

        page.on("response", handle_response)

        await page.goto(
            URL,
            wait_until="domcontentloaded",
            timeout=120000
        )

        await page.wait_for_timeout(10000)

        print(json.dumps(final_data, indent=4))

        await browser.close()

asyncio.run(main())