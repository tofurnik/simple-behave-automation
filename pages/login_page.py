from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
import settings as cfg


class LoginPage(BasePage):

    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "submit")
    ERROR_MESSAGE = (By.ID, "error")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(text(), 'successfully logged in')]")
    LOGOUT_BUTTON = (By.XPATH, "//*[contains(text(), 'Log out')]")

    def navigate(self) -> None:
        url = f"{cfg.BASE_URL}{cfg.LOGIN_PATH}"
        self.driver.get(url)
        self.wait_for_visible(self.USERNAME_INPUT)

    def enter_username(self, username: str) -> None:
        self.fill(self.USERNAME_INPUT, username)

    def enter_password(self, password: str) -> None:
        self.fill(self.PASSWORD_INPUT, password)

    def submit(self) -> None:
        self.click(self.LOGIN_BUTTON)

    def login(self, username: str, password: str) -> None:
        self.enter_username(username)
        self.enter_password(password)
        self.submit()

    def is_login_successful(self) -> bool:
        try:
            self.wait_for_url_to_contain("logged-in-successfully")
            self.wait_for_visible(self.SUCCESS_MESSAGE)
            self.wait_for_visible(self.LOGOUT_BUTTON)
            return True
        except TimeoutException:
            return False

    def get_error_message(self) -> str:
        return self.get_text(self.ERROR_MESSAGE)
