import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://web-staging.qbookapp.com/outlet/KNTEST/book-now")
    page.get_by_role("button", name="Close").click()
    page.get_by_role("button", name="Select Date").click()
    page.get_by_role("button", name="Wednesday, July 15th,").click()
    page.get_by_role("button", name="Jul 2026").click()
    page.locator("div").filter(has_text="Choose DateJuly").nth(1).click()
    page.locator("div").filter(has_text="Choose DateJuly").nth(1).click()
    page.get_by_text("Choose DateJuly").click()
    page.get_by_text("Choose DateJuly").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()
    page.get_by_role("button", name="Select Time").click()
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).nth(2).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
