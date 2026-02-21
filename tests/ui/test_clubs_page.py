"""
UI tests for the DDX Fitness clubs page.
https://www.ddxfitness.ru/clubs/
"""
import allure
import pytest
from playwright.sync_api import expect


@allure.suite("UI Tests")
@allure.feature("Clubs Page")
class TestClubsPage:

    @allure.title("Заголовок страницы 'Клубы' присутствует в DOM")
    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_clubs_page_heading_attached(self, clubs_page):
        """The h2 heading on the clubs page must be attached to the DOM."""
        expect(clubs_page.heading).to_be_attached()

    @allure.title("Заголовок страницы 'Клубы' не пустой")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    def test_clubs_page_heading_not_empty(self, clubs_page):
        """The h1 heading text must not be empty."""
        text = clubs_page.get_heading_text()
        assert text.strip(), "Clubs page h1 must not be empty"

    @allure.title("URL страницы клубов содержит '/clubs/'")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.smoke
    @pytest.mark.ui
    def test_clubs_page_url(self, clubs_page):
        """The clubs page URL must contain '/clubs/'."""
        assert "/clubs/" in clubs_page.page.url, (
            f"Expected '/clubs/' in URL, got: {clubs_page.page.url}"
        )

    @allure.title("Список клубов содержит хотя бы одну карточку")
    @allure.severity(allure.severity_level.NORMAL)
    @pytest.mark.ui
    @pytest.mark.regression
    def test_clubs_cards_loaded(self, clubs_page):
        """At least one club card must be rendered on the page."""
        # Scroll to trigger lazy-loading if needed
        clubs_page.scroll_to_bottom()
        clubs_page.page.wait_for_timeout(1_000)
        count = clubs_page.get_club_cards_count()
        assert count >= 1, (
            f"Expected at least 1 club card, found {count}"
        )

    @allure.title("Заголовок страницы клубов содержит 'DDX' или 'клуб'")
    @allure.severity(allure.severity_level.MINOR)
    @pytest.mark.ui
    def test_clubs_heading_contains_keyword(self, clubs_page):
        """Page heading must contain 'DDX', 'клуб' or 'адрес'."""
        text = clubs_page.get_heading_text().lower()
        assert any(kw in text for kw in ("клуб", "зал", "ddx", "адрес")), (
            f"Clubs heading does not contain expected keyword: '{text}'"
        )
