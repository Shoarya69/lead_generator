import asyncio
import json
import os
from playwright.async_api import async_playwright

SAVE_FOLDER = "/home/shoarya/Desktop/leadomator/app/html/google_maps_requests"

TARGET_URL = "https://www.google.com/maps/place/Zone+Gym/data=!4m7!3m6!1s0x48761be146572445:0x2d37acbbea14b2ad!8m2!3d51.5946481!4d-0.1129059!16s%2Fg%2F1yh9tz67v!19sChIJRSRXRuEbdkgRrbIU6rusNy0?authuser=0&hl=en&rclk=1"

os.makedirs(SAVE_FOLDER, exist_ok=True)

TARGET_STRINGS = [
    "zonegym.co.uk",
    "+44 20 8881 8222",
    '"4.5"',
    ">4.5<",
    "8881",
    "zonegym",
]


def safe_filename(name: str):
    invalid = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for ch in invalid:
        name = name.replace(ch, "_")
    return name[:150]


async def save_matching_response(response, index):

    try:

        url = response.url

        try:
            body = await response.text()
        except:
            return

        body_lower = body.lower()

        matched = False

        for s in TARGET_STRINGS:
            if s.lower() in body_lower:
                matched = True
                break

        if not matched:
            return

        data = {
            "matched_from": TARGET_STRINGS,
            "url": url,
            "status": response.status,
            "method": response.request.method,
            "request_headers": dict(response.request.headers),
            "response_headers": dict(response.headers),
            "post_data": response.request.post_data,
            "body": body
        }

        filename = safe_filename(
            f"MATCH_{index}_{url.split('/')[-1]}"
        )

        path = os.path.join(SAVE_FOLDER, filename + ".json")

        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4, ensure_ascii=False)

        print("\n==============================")
        print("[MATCH FOUND]")
        print(url)
        print("==============================\n")

    except Exception as e:
        print("ERROR:", e)


async def main():

    async with async_playwright() as p:

        browser = await p.chromium.launch(
            headless=False,
            args=[
                "--disable-blink-features=AutomationControlled"
            ]
        )

        context = await browser.new_context(
            viewport={"width": 1400, "height": 900}
        )

        page = await context.new_page()

        # FETCH INTERCEPT
        await page.add_init_script("""

        window.__FETCHES__ = [];

        const originalFetch = window.fetch;

        window.fetch = async (...args) => {

            const response = await originalFetch(...args);

            try {

                const clone = response.clone();

                const txt = await clone.text();

                window.__FETCHES__.push({
                    url: args[0],
                    body: txt
                });

            } catch(e){}

            return response;
        };

        """)

        counter = 0

        async def handle_response(response):
            nonlocal counter
            counter += 1
            await save_matching_response(response, counter)

        page.on("response", handle_response)

        print("Opening Google Maps...")

        await page.goto(
            TARGET_URL,
            wait_until="domcontentloaded",
            timeout=120000
        )

        await page.wait_for_timeout(15000)

        print("\n===================================")
        print("NOW MANUALLY DO THESE:")
        print("1. Scroll")
        print("2. Click About")
        print("3. Click Reviews")
        print("4. Click Website")
        print("5. Wait 30 sec")
        print("===================================\n")

        await page.wait_for_timeout(60000)

        await browser.close()


asyncio.run(main())