import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Login process
    page.goto("https://cms-staging.qbookapp.com/login")
    page.wait_for_timeout(2000)
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.wait_for_timeout(2000)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(3000)
    
    # Navigate to Time Table
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Time Table").click()
    page.wait_for_timeout(3000)
    
    # Select venue and section
    page.get_by_text("BAKU, SCBD").click()
    page.wait_for_timeout(2000)
    page.get_by_text("KN Testing").click()
    page.wait_for_timeout(2000)
    
    # Navigate and interact with timetable
    page.get_by_role("button", name="left").click()
    page.wait_for_timeout(2000)
    page.get_by_role("cell", name="appstore DEPARTED Fadlan Test").first.click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Close").click()
    page.wait_for_timeout(2000)
    
    # Logout
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(2000)
    page.get_by_text("Logout").click()
    page.wait_for_timeout(2000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)