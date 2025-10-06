import re
from playwright.sync_api import Playwright, sync_playwright, expect

# Constants
LOGIN_URL = "https://cms-staging.qbookapp.com/login"
EMAIL = "muhmmdfdln@gmail.com"
PASSWORD = "Qbook@2025"


def run(playwright: Playwright) -> None:
    # Launch browser and create page
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Navigate to login page
    page.goto(LOGIN_URL)

    # Fill login credentials
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill(EMAIL)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(PASSWORD)

    # Click Sign In button
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(10000)  # Wait for 10 seconds to ensure dashboard loads
    # Select location and user
    page.get_by_text("BAKU, SCBD").click()
    page.wait_for_timeout(3000)  # Wait for 3 seconds to ensure dashboard loads
    page.get_by_text("KN Testing").click()
    page.wait_for_timeout(10000)  # Wait for 10 seconds to ensure dashboard loads
    page.get_by_text("FAFadlan QASuper Admin (2)").click()
    page.wait_for_timeout(3000)  # Wait for 3 seconds to ensure dashboard loads
    # Logout
    page.get_by_role("menuitem", name="logout Logout").click()

    # Close browser
    context.close()
    browser.close()


if __name__ == "__main__":
    with sync_playwright() as playwright:
        run(playwright)

