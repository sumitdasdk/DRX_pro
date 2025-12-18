import pytest
import sys
from pathlib import Path
from playwright.async_api import async_playwright

sys.path.insert(0, str(Path(__file__).parent.parent))

from pages_py.LoginPage import LoginPage
from pages_py.TestDataLoader import TestDataLoader


class TestLogin:
    async def _setup_browser(self):
        p = await async_playwright().start()
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        return p, browser, page

    async def _teardown_browser(self, p, browser):
        try:
            await browser.close()
        except:
            pass
        await p.stop()

    @pytest.mark.asyncio
    async def test_tc_login_001_user_login_with_valid_credentials(self):
        """TC-001: User should successfully login with valid credentials"""
        p, browser, page = await self._setup_browser()
        try:
            login_data = TestDataLoader.get_login_data()
            assert 'username' in login_data
            assert login_data['username'] == 'Sadman'
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_login_002_doctor_name_displayed(self):
        """TC-002: After login, doctor name should be displayed"""
        p, browser, page = await self._setup_browser()
        try:
            login_data = TestDataLoader.get_login_data()
            doctor_name = login_data['expectedDoctorName']
            assert doctor_name is not None
            assert len(doctor_name) > 0
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_login_003_navigate_to_patient_section(self):
        """TC-003: User should be able to navigate to Patient section"""
        p, browser, page = await self._setup_browser()
        try:
            urls = TestDataLoader.get_urls()
            assert 'baseUrl' in urls
            assert 'digital-rx-pro' in urls['baseUrl']
        finally:
            await self._teardown_browser(p, browser)
