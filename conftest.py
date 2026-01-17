import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    login = LoginPage(page)
    login.open()
    return login

import os
from pathlib import Path

import allure
import pytest
from allure_commons.types import AttachmentType


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Получаем результат выполнения теста
    outcome = yield
    rep = outcome.get_result()

    # Нас интересует именно падение на этапе выполнения теста (call)
    if rep.when != "call" or rep.passed:
        return

    page = item.funcargs.get("page")
    if page is None:
        return

    # 1) Скриншот
    try:
        png = page.screenshot(full_page=True)
        allure.attach(png, name="screenshot", attachment_type=AttachmentType.PNG)
    except Exception:
        pass

    # 2) Trace.zip (pytest-playwright сохраняет в папку --output, обычно test-results/)
    # Попытаемся найти trace.zip рядом с артефактами текущего теста
    try:
        output_dir = Path(item.config.getoption("--output") or "test-results")
        trace_files = list(output_dir.rglob("trace.zip"))
        if trace_files:
            trace_path = trace_files[-1]
            allure.attach.file(str(trace_path), name="trace", attachment_type=AttachmentType.ZIP)
    except Exception:
        pass