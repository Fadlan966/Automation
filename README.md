# 🧪 Automation Testing Project with Playwright + Python

Project ini digunakan untuk melakukan **end-to-end automation testing** pada aplikasi berbasis web menggunakan [Playwright](https://playwright.dev/) dengan bahasa pemrograman **Python**.

---

## 📦 Prerequisites

Pastikan Anda sudah menginstal:

- Python **3.7+**
- Node.js (dibutuhkan oleh Playwright)
- pip
- Git (opsional untuk version control)

---

## 🚀 Instalasi

1. **Clone repository**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Buat virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows (PowerShell/CMD)
   source venv/Scripts/activate # Git Bash/WSL
   ```

3. **Instal dependency**
   ```bash
   pip install -r requirements.txt
   ```

4. **Instal Playwright dan browser**
   ```bash
   playwright install
   ```

---

## 🏃 Menjalankan Test

Jalankan semua test:
```bash
pytest
```

Menjalankan test file tertentu:
```bash
pytest tests/test_example.py
```

Atau bisa juga:
```bash
python testcase.py
```

---

## ✍️ Membuat Test Case dengan Codegen

Playwright menyediakan fitur **codegen** untuk merekam interaksi browser menjadi kode Python otomatis.

1. Jalankan:
   ```bash
   playwright codegen --target python -o tests/test_login.py https://alamat-website.com
   ```
2. Browser akan terbuka dan semua interaksi Anda direkam.
3. Hasil kode bisa disimpan di folder `tests/`.
4. Tambahkan **assertion/validasi** sesuai kebutuhan.

Contoh lain:
```bash
playwright codegen --target python -o test_rec.py https://example.com
```

---

## 📁 Struktur Folder

```
.
├── tests/
│   ├── test_login.py
│   ├── test_register.py
├── requirements.txt
├── README.md
```

---

## 🛠 Contoh Kode Test

```python
from playwright.sync_api import Page

def test_login_success(page: Page):
    page.goto("https://your-app.com/login")
    page.get_by_placeholder("Email").fill("user@example.com")
    page.get_by_placeholder("Password").fill("password123")
    page.get_by_role("button", name="Login").click()
    assert page.get_by_text("Dashboard").is_visible()
```

---

## 🌱 Git Workflow (Lengkap)

### 1. Membuat Branch Baru
Gunakan branch baru untuk setiap fitur/bugfix agar tidak langsung mengubah `main`.

```bash
git checkout -b nama-branch-baru
```

### 2. Melakukan Perubahan
Edit atau tambahkan file sesuai kebutuhan.

### 3. Menyimpan Perubahan (Commit)
Tambahkan file ke staging area:
```bash
git add .
```

Buat commit dengan pesan yang jelas:
```bash
git commit -m "Menambahkan test login"
```

### 4. Push ke Remote Repository
Kirim branch ke GitHub:
```bash
git push origin nama-branch-baru
```

### 5. Membuat Pull Request (PR)
1. Buka repository di GitHub.
2. Akan muncul tombol **Compare & pull request**.
3. Klik tombol tersebut, pastikan **base branch = main** dan **compare branch = nama-branch-baru**.
4. Isi judul dan deskripsi PR.
5. Klik **Create pull request**.

### 6. Review & Merge
- Reviewer akan meninjau PR Anda.
- Jika disetujui, PR bisa di-merge ke `main`.

---

## ✅ Tips

* Gunakan selector yang **spesifik** seperti `get_by_role`, `get_by_text`, atau `get_by_test_id`.
* Tambahkan `assert` untuk memverifikasi hasil test.
* Gunakan `playwright codegen` untuk mempercepat penulisan test case.
