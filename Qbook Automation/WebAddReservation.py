import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://web-staging.qbookapp.com/outlet/KNTEST/book-now")
    
    page.get_by_role("button", name="Close").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Select Date").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Today, Friday, July 10th,").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Select Time").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="14:30").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Find Availability").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Recommendations").click()
    page.wait_for_timeout(1500)
    page.get_by_text("BackConfirm Change").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="15:").click()
    page.wait_for_timeout(1500)
    page.get_by_text("BackConfirm Change").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Confirm Change").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Find Availability").click()
    page.wait_for_timeout(1500)
    
    page.get_by_role("textbox", name="Phone number* Phone number*").click()
    page.wait_for_timeout(1500)
    page.get_by_role("textbox", name="Phone number* Phone number*").fill("881012177133")
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Check Phone Number").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Continue").click()
    page.wait_for_timeout(1500)
    page.locator("rect").nth(2).click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Request Booking").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="View Booking").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Go Back").click()
    page.wait_for_timeout(1500)
    page.get_by_role("button", name="Close").click()

    # Menambahkan jeda waktu selama 1.5 detik (1500 ms)
    page.wait_for_timeout(1500)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)