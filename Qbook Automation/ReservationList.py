import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Login process
    page.goto("https://cms-staging.qbookapp.com/login")
    page.wait_for_timeout(2000)
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(3000)
    
    # Navigate to Reservation List
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Reservation List").click()
    page.wait_for_timeout(3000)
    
    # Select venue and section
    page.get_by_text("BAKU, SCBD").click()
    page.wait_for_timeout(2000)
    page.get_by_text("KN Testing").click()
    page.wait_for_timeout(2000)
    
    # Add new reservation
    page.get_by_role("button", name="plus Add Reservation").click()
    page.wait_for_timeout(2000)
    page.get_by_text("Walk In").click()
    page.wait_for_timeout(2000)
    page.get_by_title("Reservation", exact=True).locator("div").click()
    page.wait_for_timeout(2000)
    
    # Set guests
    page.get_by_text("Adult (1)").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="plus").nth(1).dblclick()
    page.wait_for_timeout(2000)
    page.get_by_label("Add Guests").get_by_role("button", name="Save").click()
    page.wait_for_timeout(2000)
    
    # Select tables
    page.locator("div").filter(has_text=re.compile(r"^No selected tables$")).nth(2).click()
    page.wait_for_timeout(2000)
    page.get_by_role("checkbox", name="B5", exact=True).check()
    page.wait_for_timeout(2000)
    page.get_by_role("checkbox", name="B6").check()
    page.wait_for_timeout(2000)
    page.get_by_label("Select Table(s) for").get_by_role("button", name="Save").click()
    page.wait_for_timeout(2000)
    
    # Select customer
    page.locator("div").filter(has_text=re.compile(r"^Customer$")).nth(2).click()
    page.wait_for_timeout(2000)
    page.get_by_role("textbox", name="Search customer by name,").fill("881012177133")
    page.wait_for_timeout(2000)
    page.get_by_text("Fadlan Test+62881012177133").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Save and Add to Reservation").click()
    page.wait_for_timeout(2000)
    
    # Set party details
    page.get_by_role("textbox", name="Input party name").fill("ITC")
    page.wait_for_timeout(2000)
    
    # Set preferences
    page.locator("div").filter(has_text=re.compile(r"^Preferences$")).nth(1).click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="down Smoking Preferences").click()
    page.wait_for_timeout(2000)
    page.get_by_text("PreviewSmoking").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="up Smoking Preferences").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Save 14 Preferences").click()
    page.wait_for_timeout(2000)
    
    # Set menu packages
    page.locator("div").filter(has_text=re.compile(r"^Menu Packages$")).nth(1).click()
    page.wait_for_timeout(2000)
    page.locator(".ant-checkbox-input").first.check()
    page.wait_for_timeout(2000)
    page.locator(".ant-row > div:nth-child(3) > .ant-btn").first.click()
    page.wait_for_timeout(2000)
    page.locator(".ant-row > div:nth-child(3) > .ant-btn").first.click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="OK").click()
    page.wait_for_timeout(2000)
    
    # Set reservation details
    page.locator(".ant-select.ant-select-outlined.ant-select-in-form-item.css-1nf76zr.ant-select-single.ant-select-allow-clear > .ant-select-selector").first.click()
    page.wait_for_timeout(2000)
    page.get_by_title("Fam").locator("div").click()
    page.wait_for_timeout(2000)
    page.get_by_text("Direct").click()
    page.wait_for_timeout(2000)
    page.get_by_title("Dinning City").locator("div").click()
    page.wait_for_timeout(2000)
    
    # Set status
    page.locator("#status").get_by_text("ACCEPTED").click()
    page.wait_for_timeout(2000)
    page.get_by_label("Choose New Status").get_by_text("CONFIRMED").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(3000)
    
    # Edit reservation status
    page.get_by_role("button", name="FadlanKuy").click()
    page.wait_for_timeout(2000)
    page.get_by_role("textbox", name="Type & enter to search by").fill("Fadlan Test")
    page.wait_for_timeout(2000) 
    page.locator(".ant-table-cell.ant-table-cell-row-hover > .anticon > svg").click()
    page.wait_for_timeout(2000)
    page.get_by_text("Edit").click()
    page.wait_for_timeout(2000)
    page.locator("#status").get_by_text("CONFIRMED").click()
    page.wait_for_timeout(2000)
    page.get_by_label("Choose New Status").get_by_text("DEPARTED").click()
    page.wait_for_timeout(2000)
    page.get_by_label("Choose New Status").get_by_role("button", name="Save").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(3000)
    
    # Logout
    page.get_by_role("button", name="FadlanKuy").click()
    page.wait_for_timeout(2000)
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(2000)
    page.get_by_text("Logout").click()
    page.wait_for_timeout(2000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)