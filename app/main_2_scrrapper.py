from playwright.async_api import async_playwright
import pandas as pd
from async_scrapper_fun import (
    titel_scraper,
    link_scraper,
    page_scroller,
    enter_op,
    results_panel_fun,
    input_box_fun
)




async def as_main_scrapper(page,query:str):
    await page.goto("https://www.google.com/maps")

    if not query:
        print("Please give some query first")
        return 

    await input_box_fun(page=page,
                        query=query)

    await enter_op(page=page)

    res = await results_panel_fun(page=page)

    await page_scroller(page=page,
                        results_panel=res)

    links = await link_scraper(page=page)

    titles = await titel_scraper(page=page)
    len_titles = len(titles)
    len_links = len(links)

    if len_titles < len_links:
        # titles kam hain → UNKNOWN se fill
        titles += ["UNKNOWN"] * (len_links - len_titles)

    return pd.DataFrame(list(zip(titles, links)), columns=["title", "link"])