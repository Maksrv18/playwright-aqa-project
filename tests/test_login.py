import os
import pytest
from playwright.sync_api import expect
import dotenv
from dotenv import load_dotenv



@pytest.mark.smoke
def test_user_can_login(login_page):
    login_page.login(
        os.getenv("VALID_USER_EMAIL"),
        os.getenv("VALID_USER_PASSWORD")
    )

    expect(login_page.page.get_by_text("You logged into a secure area!")).to_be_visible()


@allure.title("Invalid login shows error message")
@allure.severity(allure.severity_level.NORMAL)
@allure.tag("regression", "auth")
@pytest.mark.regression
def test_invalid_login_shows_error(login_page):
    login_page.open()
    login_page.login(INVALID_USER["email"], INVALID_USER["password"])

    expect(login_page.flash_message).to_be_visible()
    expect(login_page.flash_message).to_contain_text("Your username is invalid!")


@allure.title("Login button is visible on login page")
@allure.severity(allure.severity_level.MINOR)
@allure.tag("smoke", "ui")
@pytest.mark.smoke
def test_login_button_visible(login_page):
    login_page.open()

    expect(login_page.login_button).to_be_visible()