# QA Automation Framework — Selenium Python

A comprehensive test automation framework built with **Selenium WebDriver** and **Python**, 
demonstrating professional QA automation practices across multiple web applications.

---

## 🛠️ Tech Stack

- **Python 3.14**
- **Selenium WebDriver 4.x**
- **Pytest** — test framework
- **Allure Reports** — professional test reporting
- **openpyxl** — Excel data driven testing
- **webdriver-manager** — automatic driver management

---


## 📁 Repository Directory Structure

```text
.
├── config/                  # Framework configuration profiles
├── pages/                   # Page Object Model component mappings
│   ├── alert1.py            # Unified JS alert action methods
│   ├── drag_and_drop.py     # Element drag interaction definitions
│   ├── inventory_page.py    # Storefront inventory interface mapping
│   └── ...                  # Remaining isolated page views
├── tests/                   # Execution test suites and validation modules
│   ├── test_alert.py        # Functional verification tests for alerts
│   ├── test_drag_and_drop.py# UI validation assertions for components
│   └── ...                  # Remaining data-driven test cases
├── test_data/               # External CSV and Excel runtime spreadsheet inputs
├── utils/                   # Shared script definitions (logging config, file data readers)
├── conftest.py              # Centralized browser driver instantiation fixtures and hooks
├── .gitignore               # System cache and log tracking exclusions
└── README.md                # System deployment documentation guide
```

---

---

## ✅ Topics Covered

| Topic | Page Object | Test File |
|---|---|---|
| Alerts (simple, confirm, prompt) | alerts_page.py | test_alert.py |
| iFrames & Nested Frames | nested_frame.py | test_nested_frame.py |
| Dropdowns (Select class) | dropdown.py | test_dropdown.py |
| File Upload | files.py | test_file.py |
| Multiple Windows/Tabs | window_handle.py | test_window_handle.py |
| Shadow DOM (open & closed) | shadow_dom_pizza.py | test_shadow_dom_pizza.py |
| Relative Locators | relative_locator_country.py | test_relative_locator_country.py |
| Actions — Hover | hover.py | test_hover.py |
| Actions — Drag & Drop | drag_and_drop.py | test_drag_drop.py |
| Actions — Context Click | context_click.py | test_context_click.py |
| Checkboxes | checkbox.py | test_checkboxes.py |
| Dynamic Loading | dynamic_loading.py | test_dynamicloading.py |
| Keyboard Navigation | keyboard_navigation.py | test_keyboard_navigation.py |

---

## 🛒 Saucedemo E-Commerce Project

Complete end-to-end test suite for [Saucedemo](https://www.saucedemo.com):

- ✅ Login — valid, invalid, locked, empty credentials
- ✅ Inventory — page title, sorting by price, cart count
- ✅ Cart — add items, verify count, remove items
- ✅ Data driven from CSV and Excel files
- ✅ Logging to file
- ✅ Allure Reports

---

## 🚀 How to Run

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Run all tests:**
```bash
pytest tests/ -v
```

**Run on specific browser:**
```bash
pytest tests/ --browser=firefox -v
pytest tests/ --browser=chrome -v
```

**Run in headless mode:**
```bash
pytest tests/ --browser=chrome -v
# (headless enabled in conftest.py)
```

**Generate Allure report:**
```bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
```

**Generate HTML report:**
```bash
pytest tests/ --html=reports/report.html --self-contained-html -v
```

---

## 📊 Test Results

- **Total tests:** 50+
- **Pass rate:** 95%+
- **Browsers tested:** Chrome, Firefox
- **Reports:** Allure + pytest-html

---

## 📸 Screenshots

Screenshots are automatically captured on test failure and saved to `screenshots/` folder.
Also attached to Allure report for easy debugging.

---

## 🔧 Requirements

- selenium
- pytest
- pytest-html
- allure-pytest
- openpyxl
- webdriver-manager

---

## 👩‍💻 Author

**Iqra** — QA Automation Engineer  
GitHub: [iqras-dev](https://github.com/iqras-dev)