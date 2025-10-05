import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cms-staging.qbookapp.com/login")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("")
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.get_by_role("button", name="Sign In").click()
    page.goto("https://cms-staging.qbookapp.com/dashboard")
    page.wait_for_timeout(14000)
    page.get_by_text("BAKU, SCBD").click()
    page.get_by_text("KN Testing").click()
    page.get_by_text("Fadlan QA", exact=True).click()
    page.get_by_role("img", name="down").locator("svg").click()
    page.get_by_text("Logout").click()    

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
