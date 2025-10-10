import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Go to https://cms-staging.qbookapp.com/login
    page.goto("https://cms-staging.qbookapp.com/login")

    # Fill email
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.wait_for_timeout(5000)  # Wait for 5 seconds

    # Fill password
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.wait_for_timeout(5000)  # Wait for 5 seconds

    # Click Sign In
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(10000)  # Wait for 10 seconds to ensure dashboard loads
    page.wait_for_url("https://cms-staging.qbookapp.com/dashboard")

    # Open sidebar menu
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(5000)  # Wait for 5 seconds

    # Navigate to Floor Plan
    page.get_by_role("link", name="Floor Plan").click()
    page.goto(
        "https://cms-staging.qbookapp.com/reservation-floor-plan?limit=99999&offset=0&reservationStartAtStart=2025-10-09T17%3A00%3A00.000Z&reservationStartAtEnd=2025-10-10T16%3A59%3A59.999Z&brandId=2019646b-f489-4355-b8ce-e32c090b9e2b&storeId=6a2cdb92-0b72-4083-8c5c-4510b3fafb2e"
    )
    page.wait_for_timeout(10000)  # Wait for 10 seconds to ensure floor plan loads

    # Click Brand
    page.get_by_text("BAKU, SCBD").click()
    page.wait_for_timeout(3000)  # Wait for 3 seconds to ensure floor plan loads

    # Choose KN Testing
    page.get_by_text("KN Testing").click()
    page.wait_for_timeout(10000)  # Wait for 10 seconds to ensure floor plan loads

    # Double click on a reservation slot
    page.get_by_role("row", name="7:15 AM user 4 table icon B1").get_by_role("cell").nth(3).dblclick()
    page.wait_for_timeout(10000)  # Wait for 10 seconds

    page.get_by_role("button", name="Close").click()
    page.wait_for_timeout(5000)  # Wait for 5 seconds

    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(3000)  # Wait for 3 seconds

    page.get_by_text("Logout").click()

    # ---------------------
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
