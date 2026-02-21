"""
API tests for the DaData geolocation service endpoint used by DDX Fitness.
Endpoint: POST https://suggestions.dadata.ru/suggestions/api/4_1/rs/iplocate/address
"""
import allure
import pytest
import requests

from data.ddx_data import DADATA_URL


@allure.suite("API Tests")
@allure.feature("DaData Geolocation API")
class TestDadataApi:

    @allure.title("DaData endpoint доступен (200 или 401/403)")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.smoke
    def test_dadata_endpoint_reachable(self, api_client):
        """
        DaData endpoint must respond (not 5xx / timeout).
        Without a valid API key we expect 401 or 403, which still means
        the server is alive and routing correctly.
        """
        response = api_client.post(DADATA_URL, json={}, timeout=10)
        assert response.status_code in (200, 401, 403), (
            f"DaData returned unexpected status: {response.status_code}"
        )

    @allure.title("DaData endpoint возвращает JSON")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    def test_dadata_response_is_json(self, api_client):
        """DaData endpoint must return a JSON response body."""
        response = api_client.post(DADATA_URL, json={}, timeout=10)
        content_type = response.headers.get("Content-Type", "")
        assert "application/json" in content_type or response.text.startswith("{"), (
            f"Expected JSON response. Content-Type: {content_type}, "
            f"body[:100]: {response.text[:100]}"
        )

    @allure.title("DaData endpoint не возвращает 5xx")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.api
    @pytest.mark.regression
    def test_dadata_no_server_error(self, api_client):
        """DaData endpoint must not return a 5xx server error."""
        response = api_client.post(DADATA_URL, json={}, timeout=10)
        assert response.status_code < 500, (
            f"DaData returned server error: {response.status_code}"
        )

    @allure.title("DaData endpoint отвечает за разумное время (< 5 сек)")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.api
    def test_dadata_response_time(self, api_client):
        """DaData endpoint must respond within 5 seconds."""
        response = api_client.post(DADATA_URL, json={}, timeout=10)
        elapsed = response.elapsed.total_seconds()
        assert elapsed < 5.0, (
            f"DaData response took {elapsed:.2f}s (limit 5s)"
        )
