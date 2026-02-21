import allure
from playwright.sync_api import Page, Locator

from pages.base_page import BasePage


class FaqPage(BasePage):
    """Page Object for https://www.ddxfitness.ru/faq/"""

    def __init__(self, page: Page):
        super().__init__(page)

        # Page heading
        self.heading: Locator = page.locator("h1").first

        # FAQ items — clickable question rows
        self.faq_items: Locator = page.locator(
            "[class*='faq'] [class*='question'], "
            "[class*='accordion'] [class*='title'], "
            "[class*='faq-item'], details summary, "
            "[class*='FAQ'] [class*='item']"
        )

        # First question element
        self.first_question: Locator = self.faq_items.first

        # Answer / body panel that appears after clicking
        self.first_answer: Locator = page.locator(
            "[class*='faq'] [class*='answer']:first-child, "
            "[class*='accordion'] [class*='body']:first-child, "
            "details[open] > :not(summary), "
            "[class*='content']:visible"
        ).first

    # ── Actions ───────────────────────────────────────────────────────────────

    @allure.step("Open DDX Fitness FAQ page")
    def open(self):
        self.navigate("/faq/")

    @allure.step("Get FAQ page heading text")
    def get_heading_text(self) -> str:
        return self.heading.inner_text()

    @allure.step("Click first FAQ question")
    def click_first_question(self):
        self.first_question.click()

    @allure.step("Get count of FAQ items")
    def get_faq_items_count(self) -> int:
        return self.faq_items.count()
