import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=200)
    context = browser.new_context()

    # Open Login Page
    page = context.new_page()
    page.goto("https://cms-staging.qbookapp.com/login")

    # Login
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(5000)

    # Go to Floor Plan
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Floor Plan").click()
    page.wait_for_timeout(10000)

    # Choose Brand
    page.get_by_text("BAKU, SCBD").click()
    page.wait_for_timeout(5000)
    page.get_by_text("KN Testing").click()
    page.wait_for_timeout(5000)

    # Edit Reservation
    page.get_by_role("cell", name="2:00 PM").dblclick()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Edit Reservation").click()
    page.wait_for_timeout(5000)

    # Fill Form
    page.get_by_role("textbox", name="Input party name").fill("ITC")
    page.wait_for_timeout(2000)
    page.locator("div").filter(has_text=re.compile(r"^2 selections$")).nth(1).click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="down Smoking Preferences").click()
    page.get_by_text("PreviewSmoking").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="up Smoking Preferences").click()
    page.get_by_role("button", name="Save 2 Preferences").click()
    page.wait_for_timeout(2000)

    # Menu Packages
    page.locator("div").filter(has_text=re.compile(r"^Menu Packages$")).nth(1).click()
    page.wait_for_timeout(2000)
    page.locator(".ant-checkbox-input").first.check()
    page.locator(".ant-row > div:nth-child(3) > .ant-btn").first.click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="OK").click()

    # Other dropdown selections
    page.get_by_text("Mall", exact=True).click()
    page.wait_for_timeout(2000)
    page.get_by_title("Fam").locator("div").click()
    page.wait_for_timeout(2000)
    page.get_by_text("Direct").click()
    page.wait_for_timeout(2000)
    page.get_by_title("Dinning City").locator("div").click()
    page.wait_for_timeout(2000)

    # Status change and Save
    page.get_by_text("ACCEPTED").click()
    page.wait_for_timeout(2000)
    page.get_by_text("CONFIRMED").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Save").click()

    # Klik tombol terakhir
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="FadlanKuy").click()

    # Logout
    page.wait_for_timeout(5000)
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(2000)
    page.get_by_text("Logout").click()

    # Close
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
