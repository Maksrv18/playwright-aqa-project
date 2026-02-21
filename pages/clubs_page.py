import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class ClubsPage(BasePage):
    """Page Object for https://www.ddxfitness.ru/clubs/"""

    def __init__(self, page: Page):
        super().__init__(page)

        # Page heading — clubs page uses h2 (not h1) with a specific CSS class
        self.heading: Locator = page.locator(".page-main__title-clubs, h2.page-main__title-clubs").first

        # Individual club cards — each is a <li class="address__item">
        self.club_cards: Locator = page.locator("li.address__item")

        # City/metro filter buttons (if present)
        self.city_filter: Locator = page.locator(
            "[class*='filter'], [class*='Filter'], select[name*='city']"
        ).first

    # ── Actions ───────────────────────────────────────────────────────────────

    @allure.step("Open DDX Fitness clubs page")
    def open(self):
        self.navigate("/clubs/")

    @allure.step("Get page heading text")
    def get_heading_text(self) -> str:
        return self.heading.inner_text()

    @allure.step("Get number of visible club cards")
    def get_club_cards_count(self) -> int:
        return self.club_cards.count()
