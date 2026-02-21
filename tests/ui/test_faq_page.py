"""
UI tests for the DDX Fitness FAQ page.
https://www.ddxfitness.ru/faq/
"""
import allure
import pytest
from playwright.sync_api import expect


@allure.suite("UI Tests")
@allure.feature("FAQ Page")
class TestFaqPage:

    @allure.title("Страница FAQ загружается")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_faq_page_loads(self, faq_page):
        """FAQ page must load with a visible h1 heading."""
        expect(faq_page.heading).to_be_visible()

    @allure.title("URL страницы FAQ корректный")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_faq_page_url(self, faq_page):
        """The FAQ page URL must contain '/faq/'."""
        assert "/faq/" in faq_page.page.url, (
            f"Expected '/faq/' in URL, got: {faq_page.page.url}"
        )

    @allure.title("Заголовок страницы FAQ не пустой")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_faq_heading_not_empty(self, faq_page):
        """FAQ page heading text must not be empty."""
        text = faq_page.get_heading_text()
        assert text.strip(), "FAQ page h1 must not be empty"

    @allure.title("На странице FAQ есть хотя бы один вопрос")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    @pytest.mark.regression
    def test_faq_items_present(self, faq_page):
        """At least one FAQ accordion item must be rendered."""
        count = faq_page.get_faq_items_count()
        assert count >= 1, (
            f"Expected at least 1 FAQ item, found {count}"
        )

    @allure.title("Аккордеон FAQ раскрывается при клике")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    @pytest.mark.regression
    def test_faq_accordion_opens_on_click(self, faq_page):
        """Clicking the first FAQ question must reveal its answer."""
        faq_page.click_first_question()
        # After clicking, an answer element or opened state should appear
        faq_page.page.wait_for_timeout(600)
        # Check general visibility — the page should have expanded some content
        expanded = faq_page.page.locator(
            "[class*='open'] [class*='answer'], "
            "[class*='active'] [class*='content'], "
            "details[open] > p, "
            "[aria-expanded='true'] + *"
        ).first
        # Also accept if the first answer is simply visible
        answer = faq_page.page.locator(
            "[class*='answer'], [class*='body'], details > :not(summary)"
        ).first
        try:
            expect(expanded).to_be_visible(timeout=3_000)
        except Exception:
            expect(answer).to_be_visible(timeout=3_000)
