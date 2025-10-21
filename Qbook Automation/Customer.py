import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Login process
    page.goto("https://cms-staging.qbookapp.com/login")
    page.wait_for_timeout(1000)
    
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.wait_for_timeout(500)
    
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(2000)
    
    # Navigation to Customer section
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("link", name="Customer").click()
    page.wait_for_timeout(2000)
    
    # Add new customer
    page.get_by_role("button", name="plus Add Customer").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("textbox", name="8XXXXXXXXX").click()
    page.get_by_role("textbox", name="8XXXXXXXXX").fill("8810121771334414")
    page.wait_for_timeout(500)
    
    page.get_by_role("button", name="CHECK").click()
    page.wait_for_timeout(2000)
    
    # Fill customer details
    page.get_by_role("textbox", name="Input customer first name").click()
    page.get_by_role("textbox", name="Input customer first name").fill("Fadlan")
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox", name="Input customer last name").click()
    page.get_by_role("textbox", name="Input customer last name").fill("Test03414")
    page.wait_for_timeout(500)
    
    page.locator(".ant-col.ant-col-8 > .ant-form-item > .ant-row > .ant-col > .ant-form-item-control-input > .ant-form-item-control-input-content > .ant-select > .ant-select-selector > .ant-select-selection-wrap > .ant-select-selection-search").click()
    page.wait_for_timeout(500)
    
    page.get_by_title("Male", exact=True).locator("div").click()
    page.wait_for_timeout(500)
    
    page.locator(".ant-picker").click()
    page.wait_for_timeout(500)
    
    page.get_by_text("21", exact=True).click()
    page.wait_for_timeout(500)
    
    page.locator(".ant-select-selection-overflow").click()
    page.wait_for_timeout(500)
    
    page.get_by_text("‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️‼️").click()
    page.wait_for_timeout(500)
    
    page.get_by_label("Add New Customer").get_by_text("Customer Tag").click()
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox", name="Input customer memo internal").click()
    page.get_by_role("textbox", name="Input customer memo internal").fill("Ayam Goreng Sambal Terasi")
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox", name="Input customer venue memo").click()
    page.get_by_role("textbox", name="Input customer venue memo").fill("No Alcohol")
    page.wait_for_timeout(500)
    
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(2000)
    
    # Verify customer creation and close
    page.get_by_text("Detail Customer")
    page.wait_for_timeout(4000)
    
    page.get_by_role("button", name="Close").click()
    page.wait_for_timeout(1000)
    
    # Search for customer
    page.get_by_role("textbox", name="Type & enter to search by").click()
    page.get_by_role("textbox", name="Type & enter to search by").fill("Fadlan Test03414")
    page.wait_for_timeout(1000)
    
    page.goto("https://cms-staging.qbookapp.com/customer?limit=10&offset=0&search=Fadlan+")
    page.wait_for_timeout(2000)
    
    page.get_by_role("textbox", name="Type & enter to search by").fill("Fadlan Test03414")
    page.wait_for_timeout(1000)
    
    # Edit customer profile
    page.locator("tr:has-text('Fadlan Test03414') span[aria-label='more']").hover()
    page.wait_for_timeout(1000)
    
    page.get_by_text("Edit Profile").click()
    page.wait_for_timeout(1000)
    
    page.get_by_role("textbox", name="Input customer first name").click()
    page.get_by_role("textbox", name="Input customer first name").press("ControlOrMeta+a")
    page.get_by_role("textbox", name="Input customer first name").fill("Fadlan")
    page.wait_for_timeout(500)
    
    page.get_by_role("textbox", name="Input customer last name").click()
    page.get_by_role("textbox", name="Input customer last name").fill("Test0225")
    page.wait_for_timeout(500)
    
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(2000)
    
    page.get_by_role("button", name="Close", exact=True).click()
    page.wait_for_timeout(1000)
    
    # Logout process
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(1000)
    
    page.get_by_text("Logout").click()
    page.wait_for_timeout(2000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)