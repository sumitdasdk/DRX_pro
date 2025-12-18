import pytest
import sys
from pathlib import Path
from playwright.async_api import async_playwright

sys.path.insert(0, str(Path(__file__).parent.parent))

from pages_py.LoginPage import LoginPage
from pages_py.PatientPage import PatientPage
from pages_py.TestDataLoader import TestDataLoader


class TestPatient:
    """Patient test cases"""

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

    async def _login_and_navigate_to_patients(self, page):
        """Helper to login and navigate to patients page"""
        login_data = TestDataLoader.get_login_data()
        urls = TestDataLoader.get_urls()
        
        await page.goto(urls['baseUrl'])
        await LoginPage(page).login(login_data['username'], login_data['password'])
        await PatientPage(page).navigate_to_patients()

    @pytest.mark.asyncio
    async def test_tc_patient_001_navigate_to_patients(self):
        """TC-P01: User should navigate to Patients page"""
        p, browser, page = await self._setup_browser()
        try:
            await self._login_and_navigate_to_patients(page)
            assert await PatientPage(page).is_on_patient_page()
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_patient_002_create_patient(self):
        """TC-P02: User should be able to create a patient"""
        p, browser, page = await self._setup_browser()
        try:
            await self._login_and_navigate_to_patients(page)
            
            patient_data = TestDataLoader.get_patient_data('TC-P01')
            patient_name = TestDataLoader.generate_patient_name(patient_data['name'])
            patient_phone = TestDataLoader.generate_patient_phone(patient_data['phonePrefix'])
            
            await PatientPage(page).create_patient(patient_name, patient_data['age'], patient_phone)
            assert await PatientPage(page).verify_patient_displayed(patient_name)
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_patient_003_search_patient(self):
        """TC-P03: User should be able to search for patient"""
        p, browser, page = await self._setup_browser()
        try:
            await self._login_and_navigate_to_patients(page)
            
            patient_data = TestDataLoader.get_patient_data('TC-P02')
            patient_name = TestDataLoader.generate_patient_name(patient_data['name'])
            patient_phone = TestDataLoader.generate_patient_phone(patient_data['phonePrefix'])
            
            await PatientPage(page).create_patient(patient_name, patient_data['age'], patient_phone)
            await PatientPage(page).search_patient_by_name(patient_name)
            assert await PatientPage(page).verify_patient_displayed(patient_name)
        finally:
            await self._teardown_browser(p, browser)
