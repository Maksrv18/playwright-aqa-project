"""
API tests for the LeadPlan endpoint used by DDX Fitness for lead capture.
Endpoint: POST https://app.leadplan.ru/api/pageview/add
"""
import allure
import pytest

from data.ddx_data import LEADPLAN_URL, BASE_URL


@allure.suite("API Tests")
@allure.feature("LeadPlan Lead Generation API")
class TestLeadplanApi:

    @allure.title("LeadPlan endpoint доступен (не 5xx)")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.smoke
    def test_leadplan_endpoint_reachable(self, api_client):
        """
        LeadPlan pageview endpoint must respond without a 5xx server error.
        Without valid credentials/site_id we expect 400 or 401/403.
        """
        payload = {
            "url": BASE_URL,
            "referrer": "",
        }
        response = api_client.post(LEADPLAN_URL, json=payload, timeout=10)
        assert response.status_code < 500, (
            f"LeadPlan returned server error: {response.status_code}"
        )

    @allure.title("LeadPlan endpoint не возвращает 5xx при пустом теле")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.api
    @pytest.mark.regression
    def test_leadplan_empty_body_no_server_error(self, api_client):
        """Sending an empty JSON body should not cause a 5xx error."""
        response = api_client.post(LEADPLAN_URL, json={}, timeout=10)
        assert response.status_code < 500, (
            f"LeadPlan returned server error on empty body: {response.status_code}"
        )

    @allure.title("LeadPlan endpoint отвечает за разумное время (< 5 сек)")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.api
    def test_leadplan_response_time(self, api_client):
        """LeadPlan endpoint must respond within 5 seconds."""
        response = api_client.post(LEADPLAN_URL, json={}, timeout=10)
        elapsed = response.elapsed.total_seconds()
        assert elapsed < 5.0, (
            f"LeadPlan response took {elapsed:.2f}s (limit 5s)"
        )

    @allure.title("LeadPlan Content-Type ответа не является бинарным")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.api
    def test_leadplan_response_content_type(self, api_client):
        """
        LeadPlan response Content-Type must not be a binary/blob type.
        An empty Content-Type header is also acceptable (no body returned).
        """
        response = api_client.post(LEADPLAN_URL, json={}, timeout=10)
        content_type = response.headers.get("Content-Type", "")
        # Allow empty Content-Type (no body) or any text/JSON type; reject binary blobs
        assert "octet-stream" not in content_type and "application/zip" not in content_type, (
            f"LeadPlan returned unexpected binary Content-Type: {content_type}"
        )
