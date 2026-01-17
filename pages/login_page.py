import allure

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.login_button = page.get_by_role("button", name="Login")
        self.flash_message = page.locator("#flash")

    @allure.step("Open login page")
    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/login")

    @allure.step("Login as user: {username}")
    def login(self, username, password):
        self.username.fill(username)
        self.password.fill(password)
        self.login_button.click()