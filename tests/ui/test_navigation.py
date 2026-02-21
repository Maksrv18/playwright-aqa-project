"""
UI tests for header navigation on the DDX Fitness website.
Verifies that clicking navigation links takes the user to the correct pages.
"""
import allure
import pytest
from playwright.sync_api import expect

from data.ddx_data import BASE_URL, NAV_PATHS


@allure.suite("UI Tests")
@allure.feature("Navigation")
class TestNavigation:

    @allure.title("Переход на страницу 'Клубы' через навигацию")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_navigate_to_clubs(self, home_page):
        """Clicking the 'Клубы' nav link must navigate to /clubs/."""
        home_page.click_nav_clubs()
        home_page.page.wait_for_load_state("domcontentloaded")
        expect(home_page.page).to_have_url(f"{BASE_URL}/clubs/", timeout=10_000)

    @allure.title("Переход на страницу 'Тарифы' через навигацию")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_navigate_to_tariffs(self, home_page):
        """Clicking the 'Тарифы' nav link must navigate to /tarrifs/."""
        home_page.click_nav_tariffs()
        home_page.page.wait_for_load_state("domcontentloaded")
        expect(home_page.page).to_have_url(f"{BASE_URL}/tarrifs/", timeout=10_000)

    @allure.title("Все страницы в навигации доступны (parametrized)")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    @pytest.mark.regression
    @pytest.mark.parametrize("name,path", list(NAV_PATHS.items()))
    def test_all_nav_pages_reachable(self, page, name, path):
        """Each known navigation path must load without a page error."""
        url = f"{BASE_URL}{path}"
        response = page.goto(url, wait_until="domcontentloaded")
        assert response is not None and response.status < 400, (
            f"Page '{name}' at {url} returned status {response.status if response else 'None'}"
        )

    @allure.title("Кнопка 'Купить подписку' ведёт к странице тарифов")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.ui
    @pytest.mark.regression
    def test_buy_subscription_leads_to_tariffs(self, home_page):
        """'Купить подписку' CTA button must navigate to the tariffs page."""
        home_page.dismiss_cookie_banner()
        home_page.click_buy_subscription()
        home_page.page.wait_for_load_state("domcontentloaded")
        assert "/tarrifs/" in home_page.page.url or "/tariff" in home_page.page.url, (
            f"Expected to land on tariffs page, got: {home_page.page.url}"
        )
