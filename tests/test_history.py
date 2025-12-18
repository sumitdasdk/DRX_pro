import pytest
import sys
from pathlib import Path
from playwright.async_api import async_playwright

sys.path.insert(0, str(Path(__file__).parent.parent))

from pages_py.LoginPage import LoginPage
from pages_py.HistoryPage import HistoryPage
from pages_py.TestDataLoader import TestDataLoader


class TestHistory:
    """History page test cases"""

    async def _setup_browser(self):
        """Setup browser and return page object"""
        p = await async_playwright().start()
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        return p, browser, page

    async def _teardown_browser(self, p, browser):
        """Cleanup browser"""
        try:
            await browser.close()
        except:
            pass
        await p.stop()

    async def _login_and_navigate_to_history(self, page):
        """Helper to login and navigate to history page"""
        login_data = TestDataLoader.get_login_data()
        urls = TestDataLoader.get_urls()
        
        await page.goto(urls['baseUrl'])
        await LoginPage(page).login(login_data['username'], login_data['password'])
        await HistoryPage(page).navigate_to_history()

    @pytest.mark.asyncio
    async def test_tc_history_001_navigate_to_history(self):
        """TC-H-PAGE-01: User should be able to navigate to History page"""
        p, browser, page = await self._setup_browser()
        try:
            await self._login_and_navigate_to_history(page)
            assert await HistoryPage(page).is_on_history_page()
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_history_002_verify_history_table_displayed(self):
        """TC-H-PAGE-02: History table should be displayed"""
        p, browser, page = await self._setup_browser()
        try:
            await self._login_and_navigate_to_history(page)
            assert await HistoryPage(page).verify_history_table_displayed()
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_history_003_get_history_record_count(self):
        """TC-H-PAGE-03: Should be able to get history record count"""
        p, browser, page = await self._setup_browser()
        try:
            await self._login_and_navigate_to_history(page)
            record_count = await HistoryPage(page).get_history_record_count()
            assert record_count >= 0
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_history_004_history_page_complete_workflow(self):
        """TC-H-PAGE-04: Complete history page workflow"""
        p, browser, page = await self._setup_browser()
        try:
            await self._login_and_navigate_to_history(page)
            assert await HistoryPage(page).is_on_history_page()
            assert await HistoryPage(page).verify_history_table_displayed()
            record_count = await HistoryPage(page).get_history_record_count()
            assert record_count >= 0
        finally:
            await self._teardown_browser(p, browser)
