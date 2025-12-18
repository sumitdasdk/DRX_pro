import pytest
import sys
from pathlib import Path
from playwright.async_api import async_playwright

sys.path.insert(0, str(Path(__file__).parent.parent))

from pages_py.LoginPage import LoginPage
from pages_py.TestDataLoader import TestDataLoader


class TestLogin:
    """Login test cases"""

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

    @pytest.mark.asyncio
    async def test_tc_login_001_user_login_with_valid_credentials(self):
        """TC-001: User should successfully login with valid credentials"""
        p, browser, page = await self._setup_browser()
        try:
            login_data = TestDataLoader.get_login_data()
            urls = TestDataLoader.get_urls()
            
            await page.goto(urls['baseUrl'])
            await LoginPage(page).login(login_data['username'], login_data['password'])
            assert await LoginPage(page).is_logged_in()
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_login_002_doctor_name_displayed(self):
        """TC-002: After login, doctor name should be displayed"""
        p, browser, page = await self._setup_browser()
        try:
            login_data = TestDataLoader.get_login_data()
            urls = TestDataLoader.get_urls()
            
            await page.goto(urls['baseUrl'])
            await LoginPage(page).login(login_data['username'], login_data['password'])
            doctor_name = await LoginPage(page).get_doctor_name()
            assert login_data['expectedDoctorName'] in doctor_name
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_login_003_navigate_to_patient_section(self):
        """TC-003: User should be able to navigate to Patient section"""
        p, browser, page = await self._setup_browser()
        try:
            login_data = TestDataLoader.get_login_data()
            urls = TestDataLoader.get_urls()
            
            await page.goto(urls['baseUrl'])
            await LoginPage(page).login(login_data['username'], login_data['password'])
            await page.get_by_role('button', name='Patients', exact=True).click()
            await page.wait_for_url(urls['patientPagePattern'])
            assert 'doctor/patient' in page.url
        finally:
            await self._teardown_browser(p, browser)
