from playwright.sync_api import sync_playwright
import time
import pandas as pd


def main_scrapper():
    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://www.google.com/maps")

        page.wait_for_selector('input[name="q"]')

        page.fill('input[name="q"]',
                "United Kingdom Business Consultant")

        page.keyboard.press("Enter")

        page.wait_for_selector('div[role="feed"]')

        results_panel = page.locator('div[role="feed"]')

        # scroll loop
        previous_count = 0

        while True:
            results_panel.evaluate("el => el.scrollTop = el.scrollHeight")
            time.sleep(2)

            current_count = page.locator("a.hfpxzc").count()

            if current_count == previous_count:
                break

            previous_count = current_count
        # collect all business links
        links = page.locator("a.hfpxzc").all()
        titles = page.locator("div.fontHeadlineSmall").all_text_contents()
        


def titel_scraper(page):
    titles = page.locator("div.fontHeadlineSmall").all_text_contents()
    return titles

def link_scraper(page):
    links = page.locator("a.hfpxzc").all()
    return links

def page_scroller(page,results_panel):
    previous_count = 0

    while True:
        results_panel.evaluate("el => el.scrollTop = el.scrollHeight")
        time.sleep(2)

        current_count = page.locator("a.hfpxzc").count()

        if current_count == previous_count:
            break

        previous_count = current_count

def enter_op(page):
    page.keyboard.press("Enter")

def results_panel_fun(page):
    page.wait_for_selector('div[role="feed"]')

    results_panel = page.locator('div[role="feed"]')
    return results_panel

def input_box(page):
    page.wait_for_selector('input[name="q"]')

    page.fill('input[name="q"]',
                "United Kingdom Business Consultant")