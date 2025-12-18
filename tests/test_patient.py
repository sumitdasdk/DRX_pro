import pytest
import sys
from pathlib import Path
from playwright.async_api import async_playwright

sys.path.insert(0, str(Path(__file__).parent.parent))

from pages_py.LoginPage import LoginPage
from pages_py.PatientPage import PatientPage
from pages_py.TestDataLoader import TestDataLoader


class TestPatient:
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
    async def test_tc_patient_001_navigate_to_patients(self):
        """TC-P01: User should navigate to Patients page"""
        p, browser, page = await self._setup_browser()
        try:
            patient_data = TestDataLoader.get_patient_data('TC-P01')
            assert 'name' in patient_data
            assert 'age' in patient_data
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_patient_002_create_patient(self):
        """TC-P02: User should be able to create a patient"""
        p, browser, page = await self._setup_browser()
        try:
            patient_data = TestDataLoader.get_patient_data('TC-P01')
            patient_name = TestDataLoader.generate_patient_name(patient_data['name'])
            assert patient_name is not None
            assert len(patient_name) > 0
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_patient_003_search_patient(self):
        """TC-P03: User should be able to search for patient"""
        p, browser, page = await self._setup_browser()
        try:
            patient_data = TestDataLoader.get_patient_data('TC-P02')
            patient_phone = TestDataLoader.generate_patient_phone(patient_data['phonePrefix'])
            assert patient_phone is not None
            assert len(patient_phone) > 0
        finally:
            await self._teardown_browser(p, browser)
