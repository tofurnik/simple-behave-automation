from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
import settings as cfg


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self._wait = WebDriverWait(driver, cfg.TIMEOUT)

    def wait_for_visible(self, locator: tuple) -> WebElement:
        return self._wait.until(
            EC.visibility_of_element_located(locator),
            message=f"Element not visible after {cfg.TIMEOUT}s — {locator[0]}='{locator[1]}'",
        )

    def wait_for_clickable(self, locator: tuple) -> WebElement:
        return self._wait.until(
            EC.element_to_be_clickable(locator),
            message=f"Element not clickable after {cfg.TIMEOUT}s — {locator[0]}='{locator[1]}'",
        )

    def wait_for_present(self, locator: tuple) -> WebElement:
        return self._wait.until(
            EC.presence_of_element_located(locator),
            message=f"Element not present after {cfg.TIMEOUT}s — {locator[0]}='{locator[1]}'",
        )

    def wait_for_url_to_contain(self, fragment: str) -> None:
        self._wait.until(
            lambda d: fragment.lower() in d.current_url.lower(),
            message=f"URL did not contain '{fragment}' after {cfg.TIMEOUT}s — current URL: {self.driver.current_url}",
        )

    def fill(self, locator: tuple, value: str) -> None:
        field = self.wait_for_clickable(locator)
        field.clear()
        field.send_keys(value)

    def click(self, locator: tuple) -> None:
        self.wait_for_clickable(locator).click()

    def get_text(self, locator: tuple) -> str:
        return self.wait_for_visible(locator).text
