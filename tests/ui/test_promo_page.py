"""
UI tests for the DDX Fitness promotions/promo page.
https://www.ddxfitness.ru/promo/
"""
import allure
import pytest
from playwright.sync_api import expect


@allure.suite("UI Tests")
@allure.feature("Promo Page")
class TestPromoPage:

    @allure.title("Страница акций загружается")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_promo_page_loads(self, promo_page):
        """Promo page must load with a visible h1 heading."""
        expect(promo_page.heading).to_be_visible()

    @allure.title("URL страницы акций содержит '/promo/'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_promo_page_url(self, promo_page):
        """The promo page URL must contain '/promo/'."""
        assert "/promo/" in promo_page.page.url, (
            f"Expected '/promo/' in URL, got: {promo_page.page.url}"
        )

    @allure.title("Заголовок страницы акций не пустой")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.ui
    def test_promo_heading_not_empty(self, promo_page):
        """Promo page heading text must not be empty."""
        text = promo_page.get_heading_text()
        assert text.strip(), "Promo page h1 must not be empty"

    @allure.title("На странице акций есть хотя бы один элемент")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    @pytest.mark.regression
    def test_promo_items_present(self, promo_page):
        """At least one promo card/item must be rendered on the page."""
        promo_page.scroll_to_bottom()
        promo_page.page.wait_for_timeout(1_000)
        count = promo_page.get_promo_count()
        assert count >= 1, (
            f"Expected at least 1 promo item, found {count}"
        )
