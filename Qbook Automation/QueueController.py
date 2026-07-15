# import re
# from playwright.sync_api import Playwright, sync_playwright, expect


# def run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://cms-staging.qbookapp.com/login")
#     page.locator(".ant-input-affix-wrapper").first.click()
#     page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
#     page.locator(".ant-input-affix-wrapper.css-1nf76zr.ant-input-outlined.ant-input-password").click()
#     page.get_by_role("textbox", name="Password").fill("Qbook@2026")
#     page.get_by_role("button", name="Sign In").click()
#     page.get_by_role("complementary").locator("div").filter(has_text="DashboardRESERVATIONFloor").get_by_role("button").click()
#     page.get_by_role("link", name="Queue Controller").click()
#     page.locator(".ant-select-selector").click()
#     page.get_by_role("option", name="KN Testing").click()
#     page.locator("div").filter(has_text=re.compile(r"^Outdoor \(Smoking\)0 WaitingAdd$")).get_by_role("button").click()
#     page.locator("div").filter(has_text=re.compile(r"^Customer Info$")).first.click()
#     page.locator(".ant-input-affix-wrapper").click()
#     page.get_by_role("textbox", name="Search customer by name,").fill("0881012177133")
#     page.get_by_text("FadlanTest+62881012177133❤️😈").click()
#     page.get_by_label("Add Customer to Queue Number").get_by_role("button", name="Save").click()
#     page.get_by_role("button", name="Save").click()
#     page.get_by_role("dialog", name="Show QR").get_by_label("Close", exact=True).click()
#     page.get_by_text("FAFadlan QASuper Admin").click()
#     page.get_by_role("menuitem", name="logout Logout").click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     run(playwright)
