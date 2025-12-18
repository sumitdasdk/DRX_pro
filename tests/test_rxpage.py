import pytest
import sys
from pathlib import Path
from playwright.async_api import async_playwright

sys.path.insert(0, str(Path(__file__).parent.parent))

from pages_py.PrescriptionPage import PrescriptionPage
from pages_py.TestDataLoader import TestDataLoader


class TestRXPage:
    """RX Page test cases"""

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
    async def test_tc_rx_page_001_redirect_to_rx_after_login(self):
        """TC-RX-PAGE-01: User should be redirected to RX page after login"""
        p, browser, page = await self._setup_browser()
        try:
            login_data = TestDataLoader.get_login_data()
            await PrescriptionPage(page).navigate_to_rx_and_login(login_data['username'], login_data['password'])
            assert await PrescriptionPage(page).is_on_rx_page()
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_rx_page_002_create_patient_from_rx(self):
        """TC-RX-PAGE-02: Create patient from RX page successfully"""
        p, browser, page = await self._setup_browser()
        try:
            login_data = TestDataLoader.get_login_data()
            await PrescriptionPage(page).navigate_to_rx_and_login(login_data['username'], login_data['password'])
            
            rx_data = TestDataLoader.get_prescription_data('TC-RX-02')
            patient_name = TestDataLoader.generate_patient_name(rx_data['patientNamePrefix'])
            patient_phone = TestDataLoader.generate_patient_phone(rx_data['phonePrefix'])
            
            await PrescriptionPage(page).create_patient_from_rx(patient_name, rx_data['age'], patient_phone)
            assert await PrescriptionPage(page).verify_prescription_form_displayed()
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_rx_page_003_add_chief_complaint(self):
        """TC-RX-PAGE-03: Add chief complaint successfully"""
        p, browser, page = await self._setup_browser()
        try:
            login_data = TestDataLoader.get_login_data()
            await PrescriptionPage(page).navigate_to_rx_and_login(login_data['username'], login_data['password'])
            
            rx_data = TestDataLoader.get_prescription_data('TC-RX-03')
            patient_name = TestDataLoader.generate_patient_name(rx_data['patientNamePrefix'])
            patient_phone = TestDataLoader.generate_patient_phone(rx_data['phonePrefix'])
            
            await PrescriptionPage(page).create_patient_from_rx(patient_name, rx_data['age'], patient_phone)
            await PrescriptionPage(page).add_chief_complaint(rx_data['chiefComplaint'])
            assert await PrescriptionPage(page).verify_chief_complaint_field_visible()
        finally:
            await self._teardown_browser(p, browser)

    @pytest.mark.asyncio
    async def test_tc_rx_page_004_complete_workflow(self):
        """TC-RX-PAGE-04: Complete prescription workflow"""
        p, browser, page = await self._setup_browser()
        try:
            login_data = TestDataLoader.get_login_data()
            await PrescriptionPage(page).navigate_to_rx_and_login(login_data['username'], login_data['password'])
            
            rx_data = TestDataLoader.get_prescription_data('TC-RX-01')
            patient_name = TestDataLoader.generate_patient_name(rx_data['patientNamePrefix'])
            patient_phone = TestDataLoader.generate_patient_phone(rx_data['phonePrefix'])
            
            await PrescriptionPage(page).create_patient_from_rx(patient_name, rx_data['age'], patient_phone)
            await PrescriptionPage(page).add_chief_complaint(rx_data['chiefComplaint'])
            await PrescriptionPage(page).save_prescription()
        finally:
            await self._teardown_browser(p, browser)
