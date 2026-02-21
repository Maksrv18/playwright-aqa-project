"""
API tests — Site Availability.
Verifies that all main DDX Fitness pages return HTTP 200.
"""
import allure
import pytest
import requests

from data.ddx_data import BASE_URL, PUBLIC_PAGES


@allure.suite("API Tests")
@allure.feature("Site Availability")
class TestSiteAvailability:

    @allure.title("Главная страница возвращает HTTP 200")
    @allure.severity(allure.severity_level.BLOCKER)
    @pytest.mark.smoke
    @pytest.mark.api
    def test_home_page_returns_200(self, api_client):
        response = api_client.get(f"{BASE_URL}/", timeout=15)
        assert response.status_code == 200, (
            f"Home page returned {response.status_code}"
        )

    @allure.title("Страница клубов возвращает HTTP 200")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.api
    def test_clubs_page_returns_200(self, api_client):
        response = api_client.get(f"{BASE_URL}/clubs/", timeout=15)
        assert response.status_code == 200, (
            f"Clubs page returned {response.status_code}"
        )

    @allure.title("Страница тарифов возвращает HTTP 200")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.api
    def test_tariffs_page_returns_200(self, api_client):
        response = api_client.get(f"{BASE_URL}/tarrifs/", timeout=15)
        assert response.status_code == 200, (
            f"Tariffs page returned {response.status_code}"
        )

    @allure.title("Страница акций возвращает HTTP 200")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    def test_promo_page_returns_200(self, api_client):
        response = api_client.get(f"{BASE_URL}/promo/", timeout=15)
        assert response.status_code == 200, (
            f"Promo page returned {response.status_code}"
        )

    @allure.title("Страница FAQ возвращает HTTP 200")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    def test_faq_page_returns_200(self, api_client):
        response = api_client.get(f"{BASE_URL}/faq/", timeout=15)
        assert response.status_code == 200, (
            f"FAQ page returned {response.status_code}"
        )

    @allure.title("Страница заморозки возвращает HTTP 200")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    def test_freeze_page_returns_200(self, api_client):
        response = api_client.get(f"{BASE_URL}/freeze/", timeout=15)
        assert response.status_code == 200, (
            f"Freeze page returned {response.status_code}"
        )

    @allure.title("Все публичные страницы возвращают HTTP 2xx (parametrized)")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.regression
    @pytest.mark.parametrize("path", PUBLIC_PAGES)
    def test_all_public_pages_return_2xx(self, api_client, path):
        """Each public page must return a 2xx status code."""
        url = f"{BASE_URL}{path}"
        response = api_client.get(url, timeout=15)
        assert 200 <= response.status_code < 300, (
            f"Page {url} returned {response.status_code}"
        )

    @allure.title("Ответ главной страницы содержит 'DDX'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.regression
    def test_home_page_body_contains_ddx(self, api_client):
        """The HTML body of the home page must mention 'DDX'."""
        response = api_client.get(f"{BASE_URL}/", timeout=15)
        assert "DDX" in response.text, (
            "Home page HTML body does not contain 'DDX'"
        )

    @allure.title("Content-Type главной страницы содержит 'text/html'")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.api
    def test_home_page_content_type(self, api_client):
        """Home page Content-Type header must be text/html."""
        response = api_client.get(f"{BASE_URL}/", timeout=15)
        content_type = response.headers.get("Content-Type", "")
        assert "text/html" in content_type, (
            f"Unexpected Content-Type: {content_type}"
        )
