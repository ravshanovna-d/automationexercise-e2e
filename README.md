<div align="center">

# 🧪 AutomationExercise E2E Tests

**End-to-end UI test automation for [automationexercise.com](https://automationexercise.com) built with Playwright, Pytest and Allure.**

![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python&logoColor=white)
![Playwright](https://img.shields.io/badge/Playwright-1.40-2EAD33?logo=playwright&logoColor=white)
![Pytest](https://img.shields.io/badge/Pytest-7.4-0A9EDC?logo=pytest&logoColor=white)
![Allure](https://img.shields.io/badge/Report-Allure-FF6F00)
![Pattern](https://img.shields.io/badge/Pattern-Page%20Object%20Model-8A2BE2)

</div>

---

## 📌 Overview

This project automates a **complete customer purchase journey** on a demo e-commerce site, from registering a new account to placing an order. It uses the **Page Object Model** so tests stay readable and locators live in one place. Every step is recorded in an **Allure report**.

## 🧭 Tested Scenario

```
Register new user ─► Add 2 products to cart ─► Verify cart ─► Checkout ─► Pay ─► Confirm order
```

| Step | What is checked |
|---|---|
| 1. Registration | Sign up with a unique random email, fill account details, "Account Created" message |
| 2. Products | Open the catalog and add two products to the cart |
| 3. Cart | Cart contains exactly **2** items, proceed to checkout |
| 4. Checkout | Place order, enter payment details, confirm the order |

## 🧰 Tech Stack

- **Playwright** (sync API, real Google Chrome)
- **Pytest**: fixtures, markers (`e2e`, `smoke`)
- **Allure**: steps, features, severity, screenshots on failure
- **Page Object Model**: one class per page

## 📁 Project Structure

```
automationexercise-e2e/
├── pages/
│   ├── home_page.py
│   ├── registration_page.py
│   ├── products_page.py
│   ├── cart_page.py
│   └── checkout_page.py
├── tests/
│   └── test_e2e_purchase.py
├── conftest.py      # browser & page fixtures, screenshot on failure
├── pytest.ini
└── requirements.txt
```

## 🚀 Getting Started

```bash
git clone https://github.com/dlsoul13/automationexercise-e2e.git
cd automationexercise-e2e

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt
playwright install chrome
```

### Run the tests

```bash
pytest                 # all tests
pytest -m e2e          # only end-to-end tests
```

### Open the Allure report

```bash
allure serve reports/allure-results
```

> Allure CLI is required for the report: `npm i -g allure-commandline` or `scoop install allure`.

## ⚙️ Configuration

The browser setup is in `conftest.py`. By default the tests run in **headed** Chrome with `slow_mo=500` so you can watch them. For CI, set `headless=True`.

## 🗺 Roadmap

- [ ] Negative scenarios (invalid login, empty cart)
- [ ] Parallel run with `pytest-xdist`
- [ ] GitHub Actions workflow with the Allure report as an artifact
