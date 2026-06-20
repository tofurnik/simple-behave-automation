from behave import given, when, then
from pages.login_page import LoginPage
import settings as cfg


@given("I navigate to the login page")
def step_navigate_to_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()

@when("I log in with valid credentials")
def step_login_valid(context):
    context.login_page.login(cfg.USERNAME, cfg.PASSWORD)

@when("I log in with incorrect credentials")
def step_login_invalid(context):
    context.login_page.login("invalid_user@test.com", "WrongPassword123!")

@when("I log in with no credentials provided")
def step_login_invalid(context):
    context.login_page.login("", "")

@then("I should be logged in")
def step_verify_login_success(context):
    assert context.login_page.is_login_successful(), (
        f"Login failed — still on: {context.driver.current_url}"
    )

@then("I should see a login error message")
def step_verify_login_error(context):
    error = context.login_page.get_error_message()
    assert error, "Expected a login error message but none was found"
