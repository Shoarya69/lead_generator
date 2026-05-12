import asyncio
async def titel_scraper(page):
    titles = await page.locator("div.fontHeadlineSmall").all_text_contents()
    return titles

async def link_scraper(page):
    links = await page.locator("a.hfpxzc").all()
    return [await link.get_attribute("href") for link in links]

async def page_scroller(page,results_panel):
    previous_count = 0
    retry = 0
    while True:
        await results_panel.evaluate(
            "el => el.scrollTop = el.scrollHeight"
        )

        await asyncio.sleep(2)

        current_count = await page.locator("a.hfpxzc").count()

        print(f"Current count: {current_count}")

        if current_count == previous_count:

            # pehli baar same mila
            if retry == 0:
                retry += 1

                print("⏳ Waiting extra for lazy loading...")
                await asyncio.sleep(4)

                current_count = await page.locator("a.hfpxzc").count()

                if current_count == previous_count:
                    print("✅ No more new results")
                    break

            else:
                break

        else:
            retry = 0
        previous_count = current_count

async def enter_op(page):
    await page.keyboard.press("Enter")

async def results_panel_fun(page):
    try: 
        await page.wait_for_selector('div[role="feed"]')

        results_panel =  page.locator('div[role="feed"]')
        return results_panel
    except Exception as e:
        print(e)
        print("I Think no feed page appere")
async def input_box_fun(page, query):

    await page.wait_for_selector('input[name="q"]')

    await page.fill(
        'input[name="q"]',
        query
    )