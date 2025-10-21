import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Login process - Estimated time: 30 seconds
    page.goto("https://cms-staging.qbookapp.com/login")
    page.wait_for_timeout(2000)
    
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.wait_for_timeout(1000)
    
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.wait_for_timeout(1000)
    
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(3000)
    
    # Navigation to Booking Settings - Estimated time: 30 seconds
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("link", name="Booking Settings").click()
    page.wait_for_timeout(3000)
    
    # Pagination and outlet selection - Estimated time: 30 seconds
    page.get_by_text("2", exact=True).click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("row", name="FOOGU Foogu, Gunawarman Kota").locator("svg").nth(2).click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("menuitem", name="Detail").click()
    page.wait_for_timeout(3000)
    
    # Change Log inspection - Estimated time: 30 seconds
    page.get_by_text("Change Log").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("row", name="02 Oct 2025 14:46 Fadlan QA").get_by_role("button").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("tab", name="Table View").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("button", name="Close").click()
    page.wait_for_timeout(1000)
    
    # First booking settings edit - Estimated time: 1 minute
    page.get_by_text("Detail Booking Setting").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("button", name="Edit").click()
    page.wait_for_timeout(2000)
    
    # Update booking settings fields
    page.locator("#bookingSettings_further_booking_ahead").click()
    page.locator("#bookingSettings_further_booking_ahead").fill("6")
    page.wait_for_timeout(1500)
    
    page.locator("#bookingSettings_earliest_booking").click()
    page.locator("#bookingSettings_earliest_booking").fill("2")
    page.wait_for_timeout(1500)
    
    page.locator("#bookingSettings_max_online_booking_person").click()
    page.locator("#bookingSettings_max_online_booking_person").fill("10")
    page.wait_for_timeout(1500)
    
    page.locator("#bookingSettings_max_duration").click()
    page.locator("#bookingSettings_max_duration").fill("120")
    page.wait_for_timeout(1500)
    
    page.get_by_role("textbox", name="Min PAX").click()
    page.get_by_role("textbox", name="Min PAX").fill("2")
    page.wait_for_timeout(1500)
    
    page.get_by_role("textbox", name="Max PAX").click()
    page.get_by_role("textbox", name="Max PAX").fill("3")
    page.wait_for_timeout(1500)
    
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(3000)
    
    # Navigation back to booking settings list - Estimated time: 30 seconds
    page.get_by_role("list").get_by_text("Booking Setting").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("textbox", name="Search by Outlet name").click()
    page.get_by_role("textbox", name="Search by Outlet name").fill("foogu")
    pagwe.wait_for_timeout(2000)
    page.get_by_role("button", name="close-circle").click()
    page.wait_for_timeout(1000)

    # Second booking settings edit - Estimated time: 1 minute
    page.locator("#rc_select_4").click()
    page.wait_for_timeout(2000)
    
    page.get_by_text("FOOGU").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("img", name="more").locator("svg").click()
    page.wait_for_timeout(2000)
    
    page.get_by_text("Edit").click()
    page.wait_for_timeout(2000)
    
    # Update second set of booking settings
    page.locator("#bookingSettings_further_booking_ahead").click()
    page.locator("#bookingSettings_further_booking_ahead").fill("5")
    page.wait_for_timeout(1500)
    
    page.locator("#bookingSettings_max_online_booking_person").click()
    page.locator("#bookingSettings_max_online_booking_person").fill("5")
    page.wait_for_timeout(1500)
    
    page.locator("#bookingSettings_earliest_booking").click()
    page.locator("#bookingSettings_earliest_booking").fill("1")
    page.wait_for_timeout(1500)
    
    page.locator("#bookingSettings_max_duration").click()
    page.locator("#bookingSettings_max_duration").fill("60")
    page.wait_for_timeout(1500)
    
    page.get_by_role("textbox", name="Min PAX").click()
    page.get_by_role("textbox", name="Min PAX").fill("1")
    page.wait_for_timeout(1500)
    
    page.get_by_role("textbox", name="Max PAX").click()
    page.get_by_role("textbox", name="Max PAX").fill("2")
    page.wait_for_timeout(1500)
    
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(3000)
    
    # Logout process - Estimated time: 15 seconds
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("menuitem", name="logout Logout").click()
    page.wait_for_timeout(2000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)