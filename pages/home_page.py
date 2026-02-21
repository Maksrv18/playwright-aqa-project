import allure
from playwright.sync_api import Page, Locator, expect

from pages.base_page import BasePage


class HomePage(BasePage):
    """Page Object for https://www.ddxfitness.ru/ (main landing page)."""

    def __init__(self, page: Page):
        super().__init__(page)

        # ── Header / Navigation ───────────────────────────────────────────────
        self.logo: Locator = page.locator(".page-header__logo a, .logo.logo1").first
        self.nav_clubs: Locator = page.locator(
            "header a[href*='clubs'], nav a[href*='clubs']"
        ).first
        self.nav_tariffs: Locator = page.locator(
            "header a[href*='tarr'], nav a[href*='tarr']"
        ).first
        self.nav_promo: Locator = page.locator(
            "header a[href*='promo'], nav a[href*='promo']"
        ).first
        self.nav_faq: Locator = page.locator(
            "header a[href*='faq'], nav a[href*='faq']"
        ).first

        # ── CTA button (desktop — btn-orange.desk is visible in 1280px viewport) ─
        self.cta_buy_button: Locator = page.locator(
            "a.btn-orange.desk, a.btn.btn-orange.desk"
        ).first

        # ── Cookie banner ─────────────────────────────────────────────────────
        self.cookie_banner: Locator = page.locator(
            ".cookie, .cookie-banner, [class*='cookie']"
        ).first
        self.cookie_ok_btn: Locator = page.locator(
            "button:has-text('Ок'), button:has-text('OK'), "
            "button:has-text('Принять')"
        ).first

        # ── Hero / First screen ───────────────────────────────────────────────
        self.hero_heading: Locator = page.locator("h1").first

    # ── Actions ───────────────────────────────────────────────────────────────

    @allure.step("Open DDX Fitness home page")
    def open(self):
        self.navigate("/")

    @allure.step("Click 'Клубы' in header navigation")
    def click_nav_clubs(self):
        self.nav_clubs.click()

    @allure.step("Click 'Тарифы' in header navigation")
    def click_nav_tariffs(self):
        self.nav_tariffs.click()

    @allure.step("Click 'Купить подписку' CTA button")
    def click_buy_subscription(self):
        self.cta_buy_button.click()

    @allure.step("Get hero heading text")
    def get_hero_heading_text(self) -> str:
        return self.hero_heading.inner_text()
