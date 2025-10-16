import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    # Buka halaman login
    page.goto("https://cms-staging.qbookapp.com/login")
    page.wait_for_timeout(5000)

    # Login
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(8000)

    # Navigasi ke Floor Plan
    page.get_by_role("complementary").locator("div").filter(
        has_text="Main AppDashboardRESERVATIONFloor PlanReservation ListScheduleTime"
    ).get_by_role("button").click()
    page.wait_for_timeout(5000)
    page.get_by_role("link", name="Floor Plan").click()
    page.wait_for_timeout(8000)

    # Buka URL spesifik Floor Plan
    page.goto(
        "https://cms-staging.qbookapp.com/reservation-floor-plan?"
        "limit=99999&offset=0&"
        "reservationStartAtStart=2025-10-15T17%3A00%3A00.000Z&"
        "reservationStartAtEnd=2025-10-16T16%3A59%3A59.999Z&"
        "brandId=2019646b-f489-4355-b8ce-e32c090b9e2b&"
        "storeId=6a2cdb92-0b72-4083-8c5c-4510b3fafb2e"
    )
    page.wait_for_timeout(6000)

    # Pilih lokasi dan project
    page.get_by_text("BAKU, SCBD").click()
    page.wait_for_timeout(5000)
    page.get_by_role("option", name="KN Testing").click()
    page.wait_for_timeout(6000)

    # Pilih meja B10 dan B9
    page.locator("div").filter(has_text=re.compile(r"^B10$")).first.click()
    page.wait_for_timeout(5000)
    page.locator("div").filter(has_text=re.compile(r"^B9$")).first.click()
    page.wait_for_timeout(5000)

    # Tambahkan blok baru
    page.get_by_role("button", name="plus Block").click()
    page.wait_for_timeout(6000)
    page.locator("div").filter(has_text=re.compile(r"^Choose Time$")).nth(4).click()
    page.wait_for_timeout(5000)
    page.locator("div:nth-child(3) > .ant-select-item-option-content > .ant-flex").click()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(7000)

    # Klik tombol FadlanKuy
    page.get_by_role("button", name="FadlanKuy").click()
    page.wait_for_timeout(5000)

    # Edit blok arahkan kursor ke logo action
    page.get_by_text("Edit").click()
    page.wait_for_timeout(5000)
    page.locator(
        "div:nth-child(2) > .ant-modal > div > .ant-modal-content > .ant-modal-body > "
        "#form > div > div:nth-child(2) > .ant-form-item > .ant-row > "
        ".ant-col.ant-form-item-control > .ant-form-item-control-input > "
        ".ant-form-item-control-input-content > .ant-select > .ant-select-selector"
    ).click()
    page.wait_for_timeout(5000)
    page.locator("div:nth-child(5) > .ant-select-item-option-content > .ant-flex").click()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(7000)

    # Hapus blok arahkan kursor ke logo action
    page.get_by_role("button", name="FadlanKuy").click()
    page.wait_for_timeout(5000)
    page.get_by_text("Delete").click()
    page.wait_for_timeout(5000)
    page.get_by_role("button", name="OK").click()
    page.wait_for_timeout(6000)

    # Logout
    page.get_by_role("button", name="FadlanKuy").click()
    page.wait_for_timeout(5000)
    page.get_by_text("FAFadlan QASuper Admin (3)").click()
    page.wait_for_timeout(5000)
    page.get_by_text("Logout").click()
    page.wait_for_timeout(6000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
