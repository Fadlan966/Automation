import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Go to https://cms-staging.qbookapp.com/login
    page.goto("https://cms-staging.qbookapp.com/login")
    page.get_by_role("textbox", name="Email").click()

    # Fill in login credentials
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.get_by_role("button", name="Sign In").click()

    #  Go to https://cms-staging.qbookapp.com/dashboard
    page.wait_for_timeout(10000) # Wait for 10 seconds to ensure the dashboard loads completely
    page.goto("https://cms-staging.qbookapp.com/dashboard")

    # Click on the plus button to add a reservation
    page.get_by_role("button", name="plus").click()

    page.wait_for_timeout(5000) # Wait for 5 seconds to ensure the reservation modal loads completely

    # Fill in reservation details
    page.get_by_title("Walk In").click()
    page.wait_for_timeout(2000) # Wait for 2 seconds
    page.get_by_title("Reservation", exact=True).click()
    page.wait_for_timeout(2000) # Wait for 2 seconds

    # Set time
    page.locator(".ant-select.ant-select-outlined.ant-select-in-form-item.ant-select-status-success.css-1nf76zr.ant-select-focused > .ant-select-selector").click()
    page.wait_for_timeout(2000)
    page.locator("div").filter(has_text=re.compile(r"^Start$")).nth(1).click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="21:00").click()
    page.wait_for_timeout(2000)
    page.locator("div").filter(has_text=re.compile(r"^End$")).nth(1).click()
    page.wait_for_timeout(2000)
    page.get_by_role("button", name="22:00").click()
    page.wait_for_timeout(2000)
    
    # Select table
    page.get_by_text("No selected tables").click()
    page.wait_for_timeout(5000) # Wait for 5 seconds
    page.get_by_role("checkbox", name="A5", exact=True).check()
    page.wait_for_timeout(5000) # Wait for 5 seconds
    page.get_by_label("Select Table(s) for").get_by_role("button", name="Save").click()
    page.wait_for_timeout(2000) # Wait for 2 seconds

    
    # Add guests
    page.get_by_text("Adult (10)").click()
    page.wait_for_timeout(2000) # Wait for 2 seconds
    page.get_by_role("button", name="plus").nth(2).click()
    page.wait_for_timeout(5000) # Wait for 5 seconds
    page.get_by_label("Add Guests").get_by_role("button", name="Save").click()

    
    # Select customer
    page.locator("div").filter(has_text=re.compile(r"^Customer$")).nth(2).click()
    page.wait_for_timeout(2000) # Wait for 2 seconds
    page.locator(".ant-input-affix-wrapper").click()
    page.get_by_role("textbox", name="Search customer by name,").fill("881012177133")
    page.wait_for_timeout(5000) # Wait for 5 seconds
    page.get_by_text("Fadlan Test+").click()
    page.wait_for_timeout(5000) # Wait for 5 seconds
    page.get_by_role("button", name="Save and Add to Reservation").click()

    # Finalize reservation
    page.get_by_text("SEATED", exact=True).click()
    page.wait_for_timeout(2000) # Wait for 2 seconds
    page.get_by_text("ACCEPTED", exact=True).click()
    page.wait_for_timeout(2000) # Wait for 2 seconds
    page.get_by_role("button", name="Save").click()

    # Choose created reservation and logout
    page.wait_for_timeout(5000) # Wait for 5 seconds
    page.get_by_role("button", name="FadlanTest").click()
    page.wait_for_timeout(2000) # Wait for 2 seconds
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(2000) # Wait for 2 seconds
    page.get_by_text("Logout").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
