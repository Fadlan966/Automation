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
    page.get_by_role("complementary").locator("div").filter(has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime").get_by_role("button").click()
    page.get_by_role("link", name="Reservation Flag").click()
    page.get_by_text("BAKU, SCBD").click()
    page.get_by_role("option", name="KN Testing").click()
    page.get_by_role("button", name="plus Add Flag").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("TEST01")
    page.get_by_role("radio", name="Violet").check()
    page.locator("#iconName > div:nth-child(16) > div").click()
    page.get_by_role("textbox", name="Description").click()
    page.get_by_role("textbox", name="Description").fill("RORR")
    page.get_by_role("button", name="Create Flag").click()
    page.locator("svg[data-icon='more']").locator("xpath=ancestor::button").click()
    page.get_by_role("menuitem", name="Edit").click()
    page.get_by_role("textbox", name="Name").click()
    page.get_by_role("textbox", name="Name").fill("TEST012")
    page.locator("label").filter(has_text="Green").locator("span").nth(1).click()
    page.get_by_role("radio", name="Green").check()
    page.get_by_role("button", name="Update Flag").click()
    page.get_by_role("button", name="arrows-alt TEST012 RORR 06").click()
    page.get_by_role("menuitem", name="Delete", exact=True).click()
    page.get_by_role("button", name="OK").click()
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.get_by_role("menuitem", name="logout Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
