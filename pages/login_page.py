import os
import allure
from playwright.sync_api import Page, Locator


class LoginPage:
    def __init__(self, page: Page):
        self.page = page

        self.username_input: Locator = page.get_by_label("Username")
        self.password_input: Locator = page.get_by_label("Password")
        self.login_button: Locator = page.get_by_role("button", name="Login")
        self.flash_message: Locator = page.locator("#flash")

    @allure.step("Open login page")
    def open(self):
        base_url = os.getenv("BASE_URL")
        self.page.goto(f"{base_url}/login")

    @allure.step("Login as user")
    def login(self, email: str, password: str):
        self.username_input.fill(email)
        self.password_input.fill(password)
        self.login_button.click()