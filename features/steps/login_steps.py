from behave import given, when, then
from pages.login_page import LoginPage
import settings as cfg


@given("I navigate to the login page")
def navigate_to_login(context):
    context.login_page = LoginPage(context.driver)
    context.login_page.navigate()


@when("I log in with valid credentials")
def login_valid(context):
    context.login_page.login(cfg.USERNAME, cfg.PASSWORD)


@when('I log in with username "{username}" and password "{password}"')
def login_with_credentials(context, username, password):
    context.login_page.login(username, password)


@when("I log in with no credentials provided")
def login_no_credentials(context):
    context.login_page.login("", "")


@then("I should be logged in")
def verify_login_success(context):
    context.login_page.wait_for_url_to_contain("logged-in-successfully")
    context.login_page.wait_for_visible(LoginPage.SUCCESS_MESSAGE)
    context.login_page.wait_for_visible(LoginPage.LOGOUT_BUTTON)


@then("I should see a login error message")
def verify_login_error(context):
    error = context.login_page.get_error_message()
    assert error, "Expected a login error message but none was found"
