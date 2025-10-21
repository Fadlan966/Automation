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
    
    page.get_by_text("EmailPasswordForgot password?").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.wait_for_timeout(1000)
    
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(3000)
    
    # Navigation to Brand & Outlet - Estimated time: 30 seconds
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("link", name="Brand & Outlet").click()
    page.wait_for_timeout(3000)
    
    # Brand selection and management - Estimated time: 1 minute
    page.get_by_role("row", name="FOOGU eye Preview evasbr19@").get_by_label("", exact=True).check()
    page.wait_for_timeout(2000)
    
    page.get_by_role("row", name="Foogu, Gunawarman FUGW Kota").locator("svg").click()
    page.wait_for_timeout(2000)
    
    page.get_by_text("Detail").click()
    page.wait_for_timeout(3000)
    
    # Outlet Admins management - Estimated time: 1 minute
    page.get_by_role("tab", name="Outlet Admins").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("button", name="plus-circle Add Person").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("textbox", name="Person Name").click()
    page.get_by_role("textbox", name="Person Name").fill("Fadlan Test01")
    page.wait_for_timeout(1000)
    
    page.get_by_role("button", name="Add Person", exact=True).click()
    page.wait_for_timeout(3000)
    
    # Delete admin and check change log - Estimated time: 30 seconds
    page.get_by_role("row", name="Fadlan Test01 20 October 2025").get_by_role("button").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("button", name="OK").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("tab", name="Change Log").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("row", name="16 Oct 2025 23:27 Admin Farah").get_by_role("button").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("dialog", name="Detail Activity Log").get_by_label("Close", exact=True).click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("button", name="Close").click()
    page.wait_for_timeout(2000)
    
    # Search and filter operations - Estimated time: 30 seconds
    page.get_by_role("textbox", name="Search by brand name").click()
    page.get_by_role("textbox", name="Search by brand name").fill("Foogu")
    page.wait_for_timeout(2000)
    
    page.locator("#rc_select_2").first.click()
    page.wait_for_timeout(1000)
    
    page.get_by_title("evasbr19@gmail.com").locator("div").click()
    page.wait_for_timeout(2000)
    
    page.locator("div").filter(has_text=re.compile(r"^evasbr19@gmail\.comevasbr19@gmail\.com$")).locator("svg").nth(1).click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("button", name="close-circle").click()
    page.wait_for_timeout(1000)
    
    # Pagination and navigation - Estimated time: 15 seconds
    page.get_by_role("listitem", name="2").locator("a").click()
    page.wait_for_timeout(2000)
    
    page.get_by_text("1", exact=True).first.click()
    page.wait_for_timeout(2000)
    
    # Logout process - Estimated time: 15 seconds
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("menuitem", name="logout Logout").click()
    page.wait_for_timeout(3000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)