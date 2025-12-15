import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from playwright.async_api import async_playwright
from pages_py.LoginPage import LoginPage
from pages_py.HistoryPage import HistoryPage
from pages_py.TestDataLoader import TestDataLoader


@pytest.fixture(scope="function")
async def page():
    """Create a page fixture"""
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        yield page
        await browser.close()


@pytest.fixture(scope="function")
async def authenticated_page(page):
    """Create an authenticated page"""
    login_page = LoginPage(page)
    login_data = TestDataLoader.get_login_data()
    urls = TestDataLoader.get_urls()

    await page.goto(urls['baseUrl'])
    await login_page.login(login_data['username'], login_data['password'])
    return page


class TestHistory:
    """History page test cases"""

    @pytest.mark.asyncio
    async def test_tc_history_001_navigate_to_history(self, authenticated_page):
        """TC-H-PAGE-01: User should be able to navigate to History page"""
        page = authenticated_page
        history_page = HistoryPage(page)

        print('Step 1: Navigate to History page')
        await history_page.navigate_to_history()

        print('Step 2: Verify user is on history page')
        assert await history_page.is_on_history_page(), "User should be on history page"

    @pytest.mark.asyncio
    async def test_tc_history_002_verify_history_table(self, authenticated_page):
        """TC-H-PAGE-02: History table should be displayed"""
        page = authenticated_page
        history_page = HistoryPage(page)

        print('Step 1: Navigate to History page')
        await history_page.navigate_to_history()

        print('Step 2: Verify history table is displayed')
        table_visible = await history_page.verify_history_table_displayed()
        assert table_visible, "History table should be displayed"

    @pytest.mark.asyncio
    async def test_tc_history_003_get_history_record_count(self, authenticated_page):
        """TC-H-PAGE-03: Get history record count"""
        page = authenticated_page
        history_page = HistoryPage(page)

        print('Step 1: Navigate to History page')
        await history_page.navigate_to_history()

        print('Step 2: Get record count')
        count = await history_page.get_history_record_count()

        print(f'Step 3: History record count: {count}')
        assert count >= 0, "Record count should be non-negative"

    @pytest.mark.asyncio
    async def test_tc_history_004_verify_history_page_header(self, authenticated_page):
        """TC-H-PAGE-04: History page header should be visible"""
        page = authenticated_page
        history_page = HistoryPage(page)

        print('Step 1: Navigate to History page')
        await history_page.navigate_to_history()

        print('Step 2: Verify history page header is visible')
        header_visible = await history_page.verify_history_page_header_visible()
        assert header_visible, "History page header should be visible"
