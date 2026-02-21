"""
UI tests for the DDX Fitness tariffs (pricing) page.
https://www.ddxfitness.ru/tarrifs/
"""
import allure
import pytest
from playwright.sync_api import expect

from data.ddx_data import EXPECTED_TARIFF_NAMES


@allure.suite("UI Tests")
@allure.feature("Tariffs Page")
class TestTariffsPage:

    @allure.title("Страница тарифов загружается")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_tariffs_page_loads(self, tariffs_page):
        """Tariffs page must load with a visible h1 heading."""
        expect(tariffs_page.heading).to_be_visible()

    @allure.title("URL страницы тарифов корректный")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_tariffs_page_url(self, tariffs_page):
        """The tariffs page URL must contain '/tarrifs/'."""
        assert "/tarrifs/" in tariffs_page.page.url, (
            f"Expected '/tarrifs/' in URL, got: {tariffs_page.page.url}"
        )

    @allure.title("Тариф 'Infinity' виден на странице")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.regression
    def test_infinity_tariff_visible(self, tariffs_page):
        """Infinity tariff card must be visible."""
        expect(tariffs_page.infinity_card).to_be_visible()

    @allure.title("Тариф 'Smart' виден на странице")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.regression
    def test_smart_tariff_visible(self, tariffs_page):
        """Smart tariff card must be visible."""
        expect(tariffs_page.smart_card).to_be_visible()

    @allure.title("Тариф 'Light' виден на странице")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.regression
    def test_light_tariff_visible(self, tariffs_page):
        """Light tariff card must be visible."""
        expect(tariffs_page.light_card).to_be_visible()

    @allure.title("На странице тарифов есть кнопки 'Купить'")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    def test_buy_buttons_present(self, tariffs_page):
        """At least 3 'Купить' buy buttons must be present (one per plan)."""
        count = tariffs_page.get_buy_buttons_count()
        assert count >= 3, (
            f"Expected at least 3 'Купить' buttons, found {count}"
        )

    @allure.title("Все три плана (Infinity, Smart, Light) присутствуют на странице")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    @pytest.mark.parametrize("plan_name", EXPECTED_TARIFF_NAMES)
    def test_tariff_plan_names(self, tariffs_page, plan_name):
        """Each expected tariff name must appear somewhere on the page."""
        locator = tariffs_page.page.locator(f":text('{plan_name}')")
        expect(locator.first).to_be_visible(timeout=8_000)
