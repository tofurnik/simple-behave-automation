from selenium import webdriver
import settings as cfg


def before_all(context):
    if not cfg.BASE_URL:
        raise RuntimeError("base_url must be set in config.yaml before running the test suite.")
    if not cfg.USERNAME or not cfg.PASSWORD:
        raise RuntimeError("TEST_USERNAME and TEST_PASSWORD must be set in the .env file before running the test suite.")


def before_scenario(context, scenario):
    context.driver = _create_driver()
    context.driver.maximize_window()


def after_scenario(context, scenario):
    if hasattr(context, "driver") and context.driver:
        context.driver.quit()
        context.driver = None


def _create_driver() -> webdriver.Chrome:
    options = webdriver.ChromeOptions()
    if cfg.HEADLESS:
        options.add_argument("--headless=new")
    return webdriver.Chrome(options=options)

