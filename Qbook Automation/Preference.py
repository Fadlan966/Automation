import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Login process
    page.goto("https://cms-staging.qbookapp.com/login")
    page.wait_for_timeout(5000)
    
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.wait_for_timeout(4000)
    
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.wait_for_timeout(4000)
    
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(5000)
    
    # Navigation to Preferences & Package
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("link", name="Preferences & Package").click()
    page.wait_for_timeout(5000)
    
    # Add new preference
    page.get_by_role("button", name="plus Add Preference").click()
    page.wait_for_timeout(5000)
    
    page.locator("div").filter(has_text=re.compile(r"^Choose an Brand$")).nth(4).click()
    page.wait_for_timeout(4000)
    
    page.locator(".rc-virtual-list-scrollbar-thumb").click()
    page.wait_for_timeout(4000)
    
    page.get_by_title("DJOURNAL").click()
    page.wait_for_timeout(4000)
    
    page.locator(".ant-select.ant-select-outlined.ant-select-in-form-item.css-1nf76zr.ant-select-multiple > .ant-select-selector").click()
    page.wait_for_timeout(4000)
    
    page.get_by_title("KN Testing").click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("textbox", name="Preference Name", exact=True).click()
    page.get_by_role("textbox", name="Preference Name", exact=True).fill("TEST")
    page.wait_for_timeout(4000)
    
    page.locator("#preferenceTypes_0_preferenceType").click()
    page.locator("#preferenceTypes_0_preferenceType").fill("TEST010")
    page.wait_for_timeout(4000)
    
    page.locator("#preferenceTypes_0_charge").click()
    page.locator("#preferenceTypes_0_charge").fill("1.2000")
    page.wait_for_timeout(4000)
    
    page.locator("#preferenceTypes_0_minCharge").click()
    page.locator("#preferenceTypes_0_minCharge").fill("6000")
    page.wait_for_timeout(4000)
    
    page.get_by_role("button", name="delete").nth(1).click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("button", name="delete").nth(1).click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(5000)
    
    # Search and filter
    page.get_by_title("BAKU, SCBD").click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("option", name="KN Testing").click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("textbox", name="Search by Preference Name").click()
    page.get_by_role("textbox", name="Search by Preference Name").fill("TEST")
    page.wait_for_timeout(4000)
    
    # View and manage preference
    page.get_by_role("row", name="DJOURNAL KN Testing Kabupaten Aceh Singkil TEST eye Preview TEST010 Fee: 12.000").locator("svg").nth(1).click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("menuitem", name="Detail").click()
    page.wait_for_timeout(5000)
    
    page.get_by_role("tab", name="Change Log").click()
    page.wait_for_timeout(5000)
    
    page.get_by_role("button", name="Close", exact=True).click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("row", name="DJOURNAL KN Testing Kabupaten Aceh Singkil TEST eye Preview TEST010 Fee: 12.000").locator("svg").nth(1).click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("menuitem", name="Edit").click()
    page.wait_for_timeout(5000)
    
    page.get_by_role("textbox", name="Preference Name", exact=True).click()
    page.get_by_role("textbox", name="Preference Name", exact=True).fill("test12")
    page.wait_for_timeout(4000)
    
    page.get_by_role("button", name="plus Add More").click()
    page.wait_for_timeout(4000)
    
    page.locator("#preferenceTypes_1_preferenceType").click()
    page.locator("#preferenceTypes_1_preferenceType").fill("TEST9")
    page.wait_for_timeout(4000)
    
    page.locator("#preferenceTypes_1_charge").click()
    page.locator("#preferenceTypes_1_charge").fill("1.0000")
    page.wait_for_timeout(4000)
    
    page.locator("#preferenceTypes_1_minCharge").click()
    page.locator("#preferenceTypes_1_minCharge").fill("6000")
    page.wait_for_timeout(4000)
    
    page.get_by_role("button", name="Update").click()
    page.wait_for_timeout(5000)
    
    # Archive preference
    page.get_by_role("row", name="DJOURNAL KN Testing Kabupaten Aceh Singkil test12 eye Preview TEST010 Fee: 12.").locator("svg").nth(2).click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("menuitem", name="Archive").click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("button", name="OK").click()
    page.wait_for_timeout(5000)
    
    # Logout process
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(4000)
    
    page.get_by_role("menuitem", name="logout Logout").click()
    page.wait_for_timeout(5000)

    # ---------------------
    context.close()
    browser.close()
    

with sync_playwright() as playwright:
    run(playwright)