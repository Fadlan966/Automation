import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Login process
    page.goto("https://cms-staging.qbookapp.com/login")
    page.wait_for_timeout(4000)
    
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.wait_for_timeout(3000)
    
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.wait_for_timeout(3000)
    
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(4000)
    
    # Navigation to Preferences & Package
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(3000)
    
    page.get_by_role("link", name="Preferences & Package").click()
    page.wait_for_timeout(4000)
    
    page.goto("https://cms-staging.qbookapp.com/preference-and-package?limit=10&offset=0")
    page.wait_for_timeout(4000)
    
    # Switch to Packages tab
    page.get_by_role("tab", name="Packages").click()
    page.wait_for_timeout(4000)
    
    # Add new menu package
    page.get_by_role("button", name="plus Add Menu Package").click()
    page.wait_for_timeout(4000)
    
    page.locator("div").filter(has_text=re.compile(r"^Choose an Brand$")).nth(4).click()
    page.wait_for_timeout(3000)
    
    page.get_by_title("DJOURNAL").click()
    page.wait_for_timeout(3000)
    
    page.locator("div").filter(has_text=re.compile(r"^Choose an Outlet$")).nth(4).click()
    page.wait_for_timeout(3000)
    
    page.get_by_title("KN Testing").click()
    page.wait_for_timeout(3000)
    
    page.get_by_role("textbox", name="Package Code").click()
    page.get_by_role("textbox", name="Package Code").fill("test001")
    page.wait_for_timeout(3000)
    
    page.get_by_role("textbox", name="Package Name").click()
    page.get_by_role("textbox", name="Package Name").fill("test009")
    page.wait_for_timeout(3000)
    
    page.get_by_role("spinbutton", name="Price").click()
    page.get_by_role("spinbutton", name="Price").fill("1.0000")
    page.wait_for_timeout(3000)
    
    page.get_by_role("switch", name="Availability").click()
    page.wait_for_timeout(3000)
    
    page.locator(".ql-editor").click()
    page.locator(".ql-editor").fill("testdesk")
    page.wait_for_timeout(3000)
    
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(4000)
    
    # Search and filter packages
    page.get_by_role("textbox", name="Search by Package Menu").click()
    page.get_by_role("textbox", name="Search by Package Menu").fill("test")
    page.wait_for_timeout(3000)
    
    page.get_by_text("2", exact=True).click()
    page.wait_for_timeout(4000)
    
    # View and manage package
    page.get_by_role("img", name="more").locator("svg").click()
    page.wait_for_timeout(3000)
    
    page.get_by_role("menuitem", name="Detail").click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("tab", name="Change Log").click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("button", name="Close", exact=True).click()
    page.wait_for_timeout(3000)
    
    page.get_by_role("img", name="more").locator("svg").click()
    page.wait_for_timeout(3000)
    
    page.get_by_role("menuitem", name="Edit").click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("textbox", name="Package Code").click()
    page.get_by_role("textbox", name="Package Code").fill("test00112")
    page.wait_for_timeout(3000)
    
    page.get_by_role("textbox", name="Package Name").click()
    page.get_by_role("textbox", name="Package Code").fill("test001121")
    page.wait_for_timeout(3000)
    
    page.get_by_role("textbox", name="Package Name").click()
    page.get_by_role("textbox", name="Package Name").fill("test0091")
    page.wait_for_timeout(3000)
    
    page.get_by_text("testdesk").click()
    page.wait_for_timeout(3000)
    
    page.locator("div").filter(has_text=re.compile(r"^testdesk$")).nth(1).fill("testdesk01")
    page.wait_for_timeout(3000)
    
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(4000)
    
    # Archive package
    page.get_by_role("img", name="more").locator("svg").click()
    page.wait_for_timeout(3000)
    
    page.get_by_role("menuitem", name="Archive").click()
    page.wait_for_timeout(3000)
    
    page.get_by_role("button", name="OK").click()
    page.wait_for_timeout(4000)
    
    # Logout process
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(3000)
    
    page.get_by_role("menuitem", name="logout Logout").click()
    page.wait_for_timeout(4000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)