from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import TimeoutException
import settings as cfg


class BasePage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self._wait = WebDriverWait(driver, cfg.TIMEOUT)

    def wait_for_visible(self, locator: tuple) -> WebElement:
        try:
            return self._wait.until(EC.visibility_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(
                f"Element not visible after {cfg.TIMEOUT}s — {locator[0]}='{locator[1]}'"
            ) from None

    def wait_for_clickable(self, locator: tuple) -> WebElement:
        try:
            return self._wait.until(EC.element_to_be_clickable(locator))
        except TimeoutException:
            raise TimeoutException(
                f"Element not clickable after {cfg.TIMEOUT}s — {locator[0]}='{locator[1]}'"
            ) from None

    def wait_for_present(self, locator: tuple) -> WebElement:
        try:
            return self._wait.until(EC.presence_of_element_located(locator))
        except TimeoutException:
            raise TimeoutException(
                f"Element not present after {cfg.TIMEOUT}s — {locator[0]}='{locator[1]}'"
            ) from None

    def wait_for_url_to_contain(self, fragment: str) -> bool:
        try:
            return self._wait.until(
                lambda d: fragment.lower() in d.current_url.lower()
            )
        except TimeoutException:
            raise TimeoutException(
                f"URL did not contain '{fragment}' after {cfg.TIMEOUT}s — current URL: {self.driver.current_url}"
            ) from None

    def fill(self, locator: tuple, value: str) -> None:
        field = self.wait_for_clickable(locator)
        field.clear()
        field.send_keys(value)

    def click(self, locator: tuple) -> None:
        self.wait_for_clickable(locator).click()

    def get_text(self, locator: tuple) -> str:
        return self.wait_for_visible(locator).text
