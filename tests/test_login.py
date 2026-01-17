import allure
from playwright.sync_api import expect
from data.users import VALID_USER, INVALID_USER

@allure.title("User can login with valid credentials")
@allure.severity(allure.severity_level.CRITICAL)
@allure.tag("smoke", "auth")
def test_user_can_login(login_page):
    login_page.login(VALID_USER["email"], VALID_USER["password"])
    expect(login_page.page.get_by_text("You logged into a secure area!")).to_be_visible()


@allure.title("Invalid login shows error message")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression", "auth")
def test_invalid_login_shows_error(login_page):
    login_page.login(INVALID_USER["email"], INVALID_USER["password"])
    expect(login_page.flash_message).to_be_visible()
    expect(login_page.flash_message).to_contain_text("Your username is invalid!")


@allure.title("Login button is visible on login page")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("smoke", "ui")
def test_login_button_visible(login_page):
    expect(login_page.login_button).to_be_visible()