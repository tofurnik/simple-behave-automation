from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

import settings as cfg

def before_all(context):
    if not cfg.USERNAME or not cfg.PASSWORD:
        raise RuntimeError(
            "TEST_USERNAME and TEST_PASSWORD must be set in the .env file "
            "before running the test suite."
        )

def before_scenario(context, scenario):
    context.driver = _create_driver()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
        context.driver = None

def _create_driver() -> webdriver.Remote:
    browser = cfg.BROWSER.lower()

    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if cfg.HEADLESS:
            options.add_argument("--headless=new")
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )

    raise ValueError(
        f"Unsupported browser '{cfg.BROWSER}'. "
        "Set 'browser' in config/config.yaml to 'chrome'."
    )


