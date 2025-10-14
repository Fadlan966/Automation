import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    
    # goto login page
    page = context.new_page()
    page.goto("https://cms-staging.qbookapp.com/login")
    
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(10000)
    
    # go to floor plan
    page.get_by_role("complementary").locator("div").filter(has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime").get_by_role("button").click()
    page.wait_for_timeout(2000)
    page.get_by_role("link", name="Floor Plan").click()
    page.goto("https://cms-staging.qbookapp.com/reservation-floor-plan?limit=99999&offset=0&reservationStartAtStart=2025-10-12T17%3A00%3A00.000Z&reservationStartAtEnd=2025-10-13T16%3A59%3A59.999Z&brandId=2019646b-f489-4355-b8ce-e32c090b9e2b&storeId=6a2cdb92-0b72-4083-8c5c-4510b3fafb2e")
    page.wait_for_timeout(10000)
    
    # choose brand
    page.get_by_text("BAKU, SCBD").click()
    page.wait_for_timeout(5000)
    page.get_by_text("KN Testing").click()
    page.wait_for_timeout(5000)
    
    # Add Reservation
    page.locator("div").filter(has_text=re.compile(r"^B5$")).first.click()
    page.get_by_role("button", name="edit Reservation").click()
    page.wait_for_timeout(5000)
    page.get_by_text("Adult (4)").click()
    page.get_by_role("button", name="plus").first.click()
    page.get_by_role("button", name="plus").nth(1).click()
    page.wait_for_timeout(2000)
    page.get_by_label("Add Guests").get_by_role("button", name="Save").click()
    page.locator("div").filter(has_text=re.compile(r"^B5$")).nth(4).click()
    page.wait_for_timeout(2000)
    page.get_by_role("checkbox", name="B4 info-circle").check()
    page.wait_for_timeout(2000)
    page.get_by_label("Select Table(s) for").get_by_role("button", name="Save").click()
    page.wait_for_timeout(5000)
    
     # Fill Form
    page.locator("div").filter(has_text=re.compile(r"^Customer$")).nth(2).click()
    page.get_by_role("textbox", name="Search customer by name,").click()
    page.get_by_role("textbox", name="Search customer by name,").fill("881012177133")
    page.get_by_text("Fadlan Test+62881012177133No").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Save and Add to Reservation").click()
    page.wait_for_timeout(5000)
    
    # More form filling
    page.get_by_role("textbox", name="Input party name").click()
    page.get_by_role("textbox", name="Input party name").fill("ITC+")
    page.wait_for_timeout(2000)
    page.locator("div").filter(has_text=re.compile(r"^Preferences$")).nth(1).click()
    page.get_by_role("button", name="down Smoking Preferences").click()
    page.get_by_text("PreviewSmoking").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="down Service Type").click()
    page.wait_for_timeout(2000)
    page.get_by_label("Choose Preferences").get_by_text("Outdoor").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Save 2 Preferences").click()
    page.locator("div").filter(has_text=re.compile(r"^Menu Packages$")).nth(1).click()
    page.locator(".ant-checkbox-input").first.check()
    page.locator(".ant-row > div:nth-child(3) > .ant-btn").first.click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="OK").click()
    page.locator(".ant-select.ant-select-outlined.ant-select-in-form-item.css-1nf76zr.ant-select-single.ant-select-allow-clear > .ant-select-selector > .ant-select-selection-wrap > .ant-select-selection-search").first.click()
    page.wait_for_timeout(2000)
    page.get_by_title("Couple").locator("div").click()
    page.get_by_text("Direct").click()
    page.get_by_title("Dinning City").locator("div").click()
    page.get_by_text("ACCEPTED").click()
    page.wait_for_timeout(2000)
    page.get_by_text("CONFIRMED").click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="FadlanKuy").click()
    page.wait_for_timeout(5000)
    
     # Logout
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.get_by_role("menuitem", name="logout Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
