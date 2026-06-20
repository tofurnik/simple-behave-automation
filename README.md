# simple-behave-automation

A Python-based UI test automation framework using **Selenium**, **Behave** (BDD), and **Behave HTML Formatter** for reporting.

---

## Tech stack

| Tool | Purpose |
|---|---|
| [Selenium](https://www.selenium.dev/) | Browser automation |
| [Behave](https://behave.readthedocs.io/) | BDD test runner (Gherkin) |
| [behave-html-formatter](https://github.com/behave-contrib/behave-html-formatter) | Single-file HTML test report |
| [python-dotenv](https://github.com/theskumar/python-dotenv) | Load credentials from `.env` |
| [PyYAML](https://pyyaml.org/) | Load settings from `config.yaml` |

---

## Project structure

```
simple-behave-automation/
├── .env                        # Credentials — git-ignored
├── .env.example                # Credential template
├── .gitignore
├── behave.ini                  # Behave settings
├── config.yaml                 # Non-sensitive settings (URL, browser, timeout)
├── settings.py                 # Loads config.yaml + .env, exposes constants
├── requirements.txt
├── pages/
│   ├── base_page.py            # Shared wait helpers and interactions
│   └── login_page.py           # Login page object (locators + actions)
└── features/
    ├── login.feature           # Gherkin scenarios
    ├── environment.py          # Behave hooks: driver lifecycle
    └── steps/
        └── login_steps.py      # Step definitions
```

---

## Prerequisites

- Python 3.9+
- Chrome installed

---

## Setup

### 1. Install Python dependencies

```bat
pip install -r requirements.txt
```

### 2. Configure the target portal

Edit `config.yaml` and set `base_url`

### 3. Set credentials

Copy the template and fill in your test account credentials:

```bat
copy .env.example .env
```

Edit `.env`:

```
TEST_USERNAME=your_test_username
TEST_PASSWORD=your_test_password
```

## Running tests

```bat
run_tests.bat
```

Accepts any extra behave flags:

```bat
run_tests.bat --tags=smoke
run_tests.bat features/login.feature
```

### Or run the full command directly

```bat
behave -f behave_html_formatter:HTMLFormatter -o report.html
```

---

## Viewing the report


Open `report.html`.

---

## Adding a new test

1. Create `pages/my_page.py` and inherit from `BasePage`.
2. Define locators and use the inherited helpers
3. Create the corresponding feature file in `features/` and step definitions in `features/steps/`.

---

## Future improvements
- [ ] Change the report to use Allure instead of Behave HTML Formatter.
- [ ] Take a print screen on failure and embed it in the report upon failure.
- [ ] Add better error handling and logging with user-friendly messages.
- [ ] Prepare a separate DriverActions file with web interactions (waits, clicks, getting element parameters, etc.)
- [ ] Remove the python-dotenv dependency and prepare a custom method of loading credentials.
- [ ] Add support for other browsers.
- [ ] Add support for multiple environments (staging, production).
- [ ] Add support for parallel execution.


