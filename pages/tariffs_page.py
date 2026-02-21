import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class TariffsPage(BasePage):
    """Page Object for https://www.ddxfitness.ru/tarrifs/"""

    def __init__(self, page: Page):
        super().__init__(page)

        # Page heading
        self.heading: Locator = page.locator("h1").first

        # Individual tariff plan cards
        self.tariff_cards: Locator = page.locator(
            "[class*='tariff'], [class*='Tariff'], "
            "[class*='plan'], [class*='Plan'], "
            "[class*='card']"
        )

        # Named plan cards by text
        self.infinity_card: Locator = page.locator(
            ":text('Infinity'), [class*='infinity'], [class*='Infinity']"
        ).first
        self.smart_card: Locator = page.locator(
            ":text('Smart'), [class*='smart'], [class*='Smart']"
        ).first
        self.light_card: Locator = page.locator(
            ":text('Light'), [class*='light'], [class*='Light']"
        ).first

        # All 'Купить' / buy buttons on the page
        self.buy_buttons: Locator = page.locator(
            "button:has-text('Купить'), a:has-text('Купить')"
        )

    # ── Actions ───────────────────────────────────────────────────────────────

    @allure.step("Open DDX Fitness tariffs page")
    def open(self):
        self.navigate("/tarrifs/")

    @allure.step("Get page heading text")
    def get_heading_text(self) -> str:
        return self.heading.inner_text()

    @allure.step("Get count of buy buttons")
    def get_buy_buttons_count(self) -> int:
        return self.buy_buttons.count()

    @allure.step("Get all tariff plan names visible on page")
    def get_tariff_names(self) -> list[str]:
        return [
            self.page.locator(":text('Infinity')").first.inner_text(),
            self.page.locator(":text('Smart')").first.inner_text(),
            self.page.locator(":text('Light')").first.inner_text(),
        ]
