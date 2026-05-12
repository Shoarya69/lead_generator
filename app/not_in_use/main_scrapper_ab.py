from playwright.sync_api import sync_playwright
import time
import pandas as pd
from app.not_in_use.scrapper_fun import titel_scraper,link_scraper,page_scroller,enter_op,results_panel_fun,input_box_fun


def main_scrapper():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com/maps")

        input_box_fun(page=page,query="United Kingdom Business Consultant")

        enter_op(page=page)
        res = results_panel_fun(page=page)

        # scroll loop
        page_scroller(page=page,results_panel=res)
        # collect all business links
        links = link_scraper(page=page)
        titles = titel_scraper(page=page)
        return links,titles

if __name__ == "__main__":
    main_scrapper()