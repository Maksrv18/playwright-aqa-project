import allure
from playwright.sync_api import Page, Locator

from data.ddx_data import BASE_URL


class BasePage:
    """Shared helpers for all DDX Fitness page objects."""

    def __init__(self, page: Page):
        self.page = page

    # ── Navigation ────────────────────────────────────────────────────────────

    @allure.step("Navigate to {path}")
    def navigate(self, path: str = "/"):
        self.page.goto(f"{BASE_URL}{path}", wait_until="domcontentloaded")

    # ── Cookie banner ─────────────────────────────────────────────────────────

    @allure.step("Dismiss cookie banner if present")
    def dismiss_cookie_banner(self):
        """Click 'Ок' on the cookie consent banner if it is visible."""
        banner_btn: Locator = self.page.locator(
            "button:has-text('Ок'), button:has-text('OK'), "
            "button:has-text('Принять'), .cookie-accept"
        ).first
        try:
            banner_btn.click(timeout=4_000)
        except Exception:
            pass  # banner not present — fine

    # ── Scroll helpers ────────────────────────────────────────────────────────

    def scroll_to_bottom(self):
        self.page.evaluate("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_top(self):
        self.page.evaluate("window.scrollTo(0, 0)")

    # ── Generic waits ─────────────────────────────────────────────────────────

    def wait_for_network_idle(self):
        self.page.wait_for_load_state("networkidle")
