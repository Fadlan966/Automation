import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://cms-staging.qbookapp.com/login")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_role("button", name="plus").click()
    page.get_by_title("Walk In").click()
    page.get_by_title("Reservation", exact=True).click()
    page.get_by_text("No selected tables").click()
    page.get_by_role("checkbox", name="A4", exact=True).check()
    page.get_by_label("Select Table(s) for").get_by_role("button", name="Save").click()
    page.get_by_text("Adult (10)").click()
    page.get_by_role("button", name="plus").nth(2).click()
    page.get_by_label("Add Guests").get_by_role("button", name="Save").click()
    page.locator("div").filter(has_text=re.compile(r"^Customer$")).nth(2).click()
    page.locator(".ant-input-affix-wrapper").click()
    page.get_by_role("textbox", name="Search customer by name,").fill("881012177133")
    page.get_by_text("Fadlan Test+").click()
    page.get_by_role("button", name="Save and Add to Reservation").click()
    page.get_by_text("SEATED", exact=True).click()
    page.get_by_text("ACCEPTED", exact=True).click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="FadlanTest").click()
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.get_by_text("Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
