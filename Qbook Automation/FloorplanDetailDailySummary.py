import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Buka halaman login
    page.goto("https://cms-staging.qbookapp.com/login")
    page.wait_for_timeout(2000)

    # Login
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(3000)

    # Navigasi ke Floor Plan
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(1500)
    page.get_by_role("link", name="Floor Plan").click()
    page.wait_for_timeout(3000)

    # Pilih lokasi dan project
    page.get_by_text("BAKU, SCBD").click()
    page.wait_for_timeout(1000)
    page.get_by_text("KN Testing").click()
    page.wait_for_timeout(2000)

    # Interaksi dengan elemen floor plan
    page.locator("div").filter(has_text=re.compile(r"^R2P21111002200$")).first.click()
    page.wait_for_timeout(1500)
    page.get_by_role("row", name="caret-down Finished").get_by_role("button").click()
    page.wait_for_timeout(1000)
    page.get_by_role("cell", name="caret-down").click()
    page.wait_for_timeout(1000)
    page.get_by_role("cell", name="caret-up").nth(1).click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="caret-up").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="Close").click()
    page.wait_for_timeout(1500)

    # Logout
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(1000)
    page.get_by_text("Logout").click()
    page.wait_for_timeout(2000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
