import random
import re
from playwright.sync_api import Playwright, sync_playwright

# ==================== KONFIGURASI ====================
BASE_URL = "https://cms-staging.qbookapp.com/login"
EMAIL = "muhmmdfdln@gmail.com"
PASSWORD = "Qbook@2026"
OUTLET_NAME = "KN Testing"
CUSTOMER_PHONE = "0881012177133"

QUEUE_CATEGORIES = [
    "Family/Group Table",
    "Outdoor (Smoking)",
    "Indoor",
    "Rebels",
    "Training",
]

SLOW_MO_MS = 800
CHECKPOINT_MS = 1000


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False, slow_mo=SLOW_MO_MS)
    context = browser.new_context()
    page = context.new_page()

    # ---------- 1. Login ----------
    print("[1/7] Login...")
    page.goto(BASE_URL)
    page.locator(".ant-input-affix-wrapper").first.click()
    page.get_by_role("textbox", name="Email").fill(EMAIL)
    page.locator(".ant-input-affix-wrapper.css-1nf76zr.ant-input-outlined.ant-input-password").click()
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(CHECKPOINT_MS)

    # ---------- 2. Buka menu Queue Controller ----------
    print("[2/7] Buka Queue Controller...")
    page.get_by_role("complementary").locator("div").filter(
        has_text="DashboardRESERVATIONFloor"
    ).get_by_role("button").click()
    page.get_by_role("link", name="Queue Controller").click()
    page.wait_for_timeout(CHECKPOINT_MS)

    # ---------- 3. Pilih outlet ----------
    print(f"[3/7] Pilih outlet: {OUTLET_NAME}...")
    page.locator(".ant-select-selector").click()
    page.get_by_role("option", name=OUTLET_NAME).click()
    page.wait_for_timeout(CHECKPOINT_MS)

    # ---------- 4. Tambah antrian (kategori dipilih acak) ----------
    selected_category = random.choice(QUEUE_CATEGORIES)
    print(f"[4/7] Tambah antrian ke kategori: {selected_category}...")
    category_pattern = re.compile(rf"^{re.escape(selected_category)}")
    category_card = page.locator("div").filter(
        has_text=category_pattern
    ).filter(has=page.get_by_role("button", name="Add")).first
    category_card.get_by_role("button", name="Add").click()
    page.wait_for_timeout(CHECKPOINT_MS)

    # ---------- 5. Isi Customer Info ----------
    print("[5/7] Isi data customer...")
    page.locator("div").filter(has_text=re.compile(r"^Customer Info$")).first.click()
    page.locator(".ant-input-affix-wrapper").click()
    page.get_by_role("textbox", name="Search customer by name,").fill(CUSTOMER_PHONE)
    page.get_by_text("FadlanTest+62881012177133❤️😈").click()
    page.get_by_label("Add Customer to Queue Number").get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Save").click()
    page.wait_for_timeout(CHECKPOINT_MS)

    # ---------- 6. Tutup dialog QR ----------
    print("[6/7] Tutup dialog QR...")
    page.get_by_role("dialog", name="Show QR").get_by_label("Close", exact=True).click()
    page.wait_for_timeout(CHECKPOINT_MS)

    # ---------- 7. Logout ----------
    print("[7/7] Logout...")
    page.get_by_text("FAFadlan QASuper Admin").click()
    page.get_by_role("menuitem", name="logout Logout").click()
    page.wait_for_timeout(CHECKPOINT_MS)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)