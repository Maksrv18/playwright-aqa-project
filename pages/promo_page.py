import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class PromoPage(BasePage):
    """Page Object for https://www.ddxfitness.ru/promo/"""

    def __init__(self, page: Page):
        super().__init__(page)

        # Page heading
        self.heading: Locator = page.locator("h1").first

        # Promo cards/items — each is an <a class="advantages__content js-link-to-pop-up">
        self.promo_items: Locator = page.locator(".advantages__content")

    # ── Actions ───────────────────────────────────────────────────────────────

    @allure.step("Open DDX Fitness promo page")
    def open(self):
        self.navigate("/promo/")

    @allure.step("Get promo page heading text")
    def get_heading_text(self) -> str:
        return self.heading.inner_text()

    @allure.step("Get count of promo items")
    def get_promo_count(self) -> int:
        return self.promo_items.count()
