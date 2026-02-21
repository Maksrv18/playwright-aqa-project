import pytest
import requests
import os
from pathlib import Path

import allure
from allure_commons.types import AttachmentType
from dotenv import load_dotenv
from playwright.sync_api import Page

from pages.home_page import HomePage
from pages.clubs_page import ClubsPage
from pages.tariffs_page import TariffsPage
from pages.faq_page import FaqPage
from pages.promo_page import PromoPage

load_dotenv()

# ──────────────────────────────────────────────
# Browser / context settings
# ──────────────────────────────────────────────

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Override default context: viewport, locale, user-agent."""
    return {
        **browser_context_args,
        "viewport": {"width": 1280, "height": 720},
        "locale": "ru-RU",
        "ignore_https_errors": True,
    }


# ──────────────────────────────────────────────
# DDX Fitness — page fixtures
# ──────────────────────────────────────────────

@pytest.fixture
def home_page(page: Page):
    hp = HomePage(page)
    hp.open()
    return hp


@pytest.fixture
def clubs_page(page: Page):
    cp = ClubsPage(page)
    cp.open()
    return cp


@pytest.fixture
def tariffs_page(page: Page):
    tp = TariffsPage(page)
    tp.open()
    return tp


@pytest.fixture
def faq_page(page: Page):
    fp = FaqPage(page)
    fp.open()
    return fp


@pytest.fixture
def promo_page(page: Page):
    pp = PromoPage(page)
    pp.open()
    return pp


# ──────────────────────────────────────────────
# API fixture
# ──────────────────────────────────────────────

@pytest.fixture(scope="session")
def api_client():
    """Requests session with common headers for API tests."""
    session = requests.Session()
    session.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json",
        "User-Agent": "DDX-AQA-Bot/1.0",
    })
    yield session
    session.close()


# ──────────────────────────────────────────────
# Allure: screenshot + trace on failure
# ──────────────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when != "call" or rep.passed:
        return

    page: Page | None = item.funcargs.get("page")
    if page is None:
        return

    try:
        png = page.screenshot(full_page=True)
        allure.attach(png, name="screenshot", attachment_type=AttachmentType.PNG)
    except Exception:
        pass

    try:
        output_dir = Path(item.config.getoption("--output") or "test-results")
        trace_files = list(output_dir.rglob("trace.zip"))
        if trace_files:
            allure.attach.file(
                str(trace_files[-1]),
                name="trace",
                attachment_type=AttachmentType.ZIP,
            )
    except Exception:
        pass