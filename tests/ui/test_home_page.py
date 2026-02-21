"""
UI tests for the DDX Fitness home page.
https://www.ddxfitness.ru/
"""
import allure
import pytest
from playwright.sync_api import expect


@allure.suite("UI Tests")
@allure.feature("Home Page")
class TestHomePage:

    @allure.title("Заголовок страницы содержит 'DDX'")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_page_title_contains_ddx(self, home_page):
        """Page <title> must contain 'DDX' (case-insensitive)."""
        title = home_page.page.title()
        assert "DDX" in title.upper(), (
            f"Expected 'DDX' in page title, got: '{title}'"
        )

    @allure.title("Логотип виден в шапке")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_logo_is_visible(self, home_page):
        """Header logo must be visible."""
        expect(home_page.logo).to_be_visible()

    @allure.title("Кнопка 'Купить подписку' видна")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_cta_buy_button_is_visible(self, home_page):
        """CTA 'Купить подписку' button in the header must be visible."""
        expect(home_page.cta_buy_button).to_be_visible()

    @allure.title("Ссылка 'Клубы' видна в навигации")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_nav_clubs_link_visible(self, home_page):
        """'Клубы' navigation link must be visible in the header."""
        expect(home_page.nav_clubs).to_be_visible()

    @allure.title("Ссылка 'Тарифы' видна в навигации")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_nav_tariffs_link_visible(self, home_page):
        """'Тарифы' navigation link must be visible in the header."""
        expect(home_page.nav_tariffs).to_be_visible()

    @allure.title("Главный заголовок (h1) не пустой")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_hero_heading_not_empty(self, home_page):
        """The primary <h1> heading on the home page must not be empty."""
        text = home_page.get_hero_heading_text()
        assert text.strip(), "Hero h1 heading must not be empty"

    @allure.title("Cookie-баннер скрывается после нажатия 'Ок'")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.ui
    @pytest.mark.regression
    def test_cookie_banner_dismissible(self, home_page):
        """Cookie banner should disappear after the user clicks 'Ок'."""
        # The page is already loaded; check whether the banner appears and dismiss it
        home_page.dismiss_cookie_banner()
        # After dismissal the cookie button itself should be gone / no longer visible
        expect(home_page.cookie_ok_btn).not_to_be_visible(timeout=5_000)

    @allure.title("URL главной страницы корректный")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_home_page_url(self, home_page):
        """Page URL must be the DDX Fitness domain."""
        assert "ddxfitness.ru" in home_page.page.url, (
            f"Unexpected URL: {home_page.page.url}"
        )
