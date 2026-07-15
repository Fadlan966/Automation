import re
from playwright.sync_api import Playwright, sync_playwright

PHONE_NUMBER = "88975264915"
                # "881012177133"

def booking(page):
    page.goto("https://web-staging.qbookapp.com/outlet/KNTEST/book-now")

    # Close popup
    page.get_by_role("button", name="Close").click()

    # Select Date
    page.get_by_role("button", name="Select Date").click()
    page.get_by_role("button", name="Thursday, July 16th,").click()

    # Select Time
    page.get_by_role("button", name="Select Time").click()
    page.get_by_role("button", name="15:30").click()
    # page.get_by_role("button", name="16:30").click()
    # page.get_by_role("button", name="19:00").click()
    # Find Availability
    page.get_by_role("button", name="Find Availability").click()

    # # Recommendation
    # page.get_by_role("button", name="Recommendations").click()
    # page.get_by_text("BackConfirm Change").click()

    # page.get_by_role("button", name="15:").click()
    # page.get_by_text("BackConfirm Change").click()
    # page.get_by_role("button", name="Confirm Change").click()

    # page.get_by_role("button", name="Find Availability").click()

    # Phone Number
    phone = page.get_by_role("textbox", name="Phone number* Phone number*")
    phone.click()
    phone.fill(PHONE_NUMBER)

    page.get_by_role("button", name="Check Phone Number").click()
    page.get_by_role("button", name="Continue").click()

    # Signature
    page.locator("rect").nth(2).click()

    # Request Booking
    page.get_by_role("button", name="Request Booking").click()

    # View Booking
    page.get_by_role("button", name="View Booking").click()

    # Back
    page.get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("button", name="Go Back").click()
    page.get_by_role("button", name="Close").click()


def run(playwright: Playwright):
    browser = playwright.chromium.launch(
        headless=False,
        slow_mo=300  # agar pergerakan browser lebih terlihat
    )

    for i in range(39):
        print("=" * 50)
        print(f"TEST BOOKING KE-{i+1}")
        print("=" * 50)

        context = browser.new_context()
        page = context.new_page()

        try:
            booking(page)
            print(f"✅ Booking ke-{i+1} BERHASIL")

        except Exception as e:
            print(f"❌ Booking ke-{i+1} GAGAL")
            print(e)

        finally:
            context.close()

    browser.close()


with sync_playwright() as playwright:
    run(playwright)