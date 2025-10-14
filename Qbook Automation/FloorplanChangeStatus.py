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
    page.get_by_role("link", name="Floor Plan").click()
    page.get_by_text("BAKU, SCBD").click()
    page.get_by_text("KN Testing").click()
    page.get_by_text("CONFIRMED").nth(1).click()
    page.get_by_text("DEPARTED").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_text("CONFIRMED").click()
    page.get_by_text("ACCEPTED").click()
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.get_by_text("Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
