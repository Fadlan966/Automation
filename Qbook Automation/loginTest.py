import time
import re
from playwright.sync_api import Playwright, sync_playwright, expect

def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    
    # Buka halaman login
    page.goto("https://cms-staging.qbookapp.com/login")

    # Isi email dan password
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("muhmmdfdln@gmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("Qbook@2025")

    # Klik tombol Sign In
    page.get_by_role("button", name="Sign In").click()

    # Tunggu beberapa detik agar login selesai & dashboard termuat
    page.wait_for_timeout(10000) # Tunggu 10 detik

    # Klik profil dan logout
    page.get_by_text("Fadlan QA", exact=True).click()
    page.wait_for_timeout(3000) # Tunggu 3 detik
    page.get_by_role("img", name="down").locator("svg").click()
    page.get_by_text("Logout").click()

    # Tutup browser
    context.close()
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
