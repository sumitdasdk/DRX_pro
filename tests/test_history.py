import pytest
import sys
from pathlib import Path
from playwright.async_api import async_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from pages_py.LoginPage import LoginPage
from pages_py.HistoryPage import HistoryPage
from pages_py.TestDataLoader import TestDataLoader


class TestHistory:
    """History page test cases"""

    async def _login_and_navigate_to_history(self, page):
        """Helper to login and navigate to history page"""
        login_page = LoginPage(page)
        login_data = TestDataLoader.get_login_data()
        urls = TestDataLoader.get_urls()

        await page.goto(urls['baseUrl'])
        await login_page.login(login_data['username'], login_data['password'])
        
        history_page = HistoryPage(page)
        await history_page.navigate_to_history()
        return history_page

    @pytest.mark.asyncio
    async def test_tc_history_001_navigate_to_history(self):
        """TC-H-PAGE-01: User should be able to navigate to History page"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                history_page = await self._login_and_navigate_to_history(page)
                assert await history_page.is_on_history_page(), "User should be on history page"
                print("✓ TC-H-PAGE-01 PASSED: Navigate to history page")
            except Exception as e:
                print(f"❌ TC-H-PAGE-01 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_tc_history_002_verify_history_table_displayed(self):
        """TC-H-PAGE-02: History table should be displayed"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                history_page = await self._login_and_navigate_to_history(page)
                table_displayed = await history_page.verify_history_table_displayed()
                assert table_displayed, "History table should be displayed"
                print("✓ TC-H-PAGE-02 PASSED: History table displayed")
            except Exception as e:
                print(f"❌ TC-H-PAGE-02 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_tc_history_003_get_history_record_count(self):
        """TC-H-PAGE-03: Should be able to get history record count"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                history_page = await self._login_and_navigate_to_history(page)
                record_count = await history_page.get_history_record_count()
                assert record_count >= 0, "Record count should be non-negative"
                print(f"✓ TC-H-PAGE-03 PASSED: History record count: {record_count}")
            except Exception as e:
                print(f"❌ TC-H-PAGE-03 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_tc_history_004_history_page_complete_workflow(self):
        """TC-H-PAGE-04: Complete history page workflow"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                history_page = await self._login_and_navigate_to_history(page)
                
                # Verify we're on the history page
                assert await history_page.is_on_history_page(), "Should be on history page"
                
                # Verify history table is displayed
                table_displayed = await history_page.verify_history_table_displayed()
                assert table_displayed, "History table should be displayed"
                
                # Get record count
                record_count = await history_page.get_history_record_count()
                assert record_count >= 0, "Record count should be non-negative"
                
                print(f"✓ TC-H-PAGE-04 PASSED: Complete workflow with {record_count} records")
            except Exception as e:
                print(f"❌ TC-H-PAGE-04 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass
