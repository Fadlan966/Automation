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
    page.locator("div").filter(has_text=re.compile(r"^Limited$")).first.click()
    page.get_by_role("button", name="plus Add Config").click()
    page.get_by_role("textbox", name="Meal Time").click()
    page.get_by_role("textbox", name="Meal Time").fill("TEST Dinner")
    page.get_by_role("combobox", name="Icon").click()
    page.locator("div").filter(has_text=re.compile(r"^Dinner$")).nth(2).click()
    page.get_by_role("textbox", name="Time Range").click()
    page.get_by_text("22").first.click()
    page.get_by_text("40", exact=True).click()
    page.get_by_role("textbox", name="End time").click()
    page.get_by_text("23").first.click()
    page.get_by_text("15").nth(1).click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("row", name="TEST Dinner 22:40 - 23:15 more").get_by_role("switch").click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("row", name="TEST Dinner 22:40 - 23:15 more").get_by_role("switch").click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("row", name="TEST Dinner 22:40 - 23:15 more").locator("svg").nth(1).click()
    page.get_by_text("Edit").click()
    page.get_by_role("textbox", name="Meal Time").click()
    page.get_by_role("textbox", name="Meal Time").fill("TEST Dinner01")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("row", name="TEST Dinner01 22:40 - 23:15").locator("svg").nth(1).click()
    page.get_by_text("Delete").click()
    page.get_by_role("button", name="OK").click()
    page.get_by_role("button", name="Close").click()
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.get_by_text("Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
