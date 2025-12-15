import pytest
import sys
from pathlib import Path
from playwright.async_api import async_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from pages_py.PrescriptionPage import PrescriptionPage
from pages_py.TestDataLoader import TestDataLoader


class TestRXPage:
    """RX Page test cases"""

    @pytest.mark.asyncio
    async def test_tc_rx_page_001_redirect_to_rx_after_login(self):
        """TC-RX-PAGE-01: User should be redirected to RX page after login"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                rx_page = PrescriptionPage(page)
                login_data = TestDataLoader.get_login_data()

                print('Step 1: Login to RX page')
                await rx_page.navigate_to_rx_and_login(login_data['username'], login_data['password'])

                print('Step 2: Verify user is on RX page')
                assert await rx_page.is_on_rx_page(), "User should be on RX page"
                print("✓ TC-RX-PAGE-01 PASSED")
            except Exception as e:
                print(f"❌ TC-RX-PAGE-01 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_tc_rx_page_002_create_patient_from_rx(self):
        """TC-RX-PAGE-02: Create patient from RX page successfully"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                rx_page = PrescriptionPage(page)
                login_data = TestDataLoader.get_login_data()

                print('Step 1: Login to RX page')
                await rx_page.navigate_to_rx_and_login(login_data['username'], login_data['password'])

                print('Step 2: Create patient')
                rx_data = TestDataLoader.get_prescription_data('TC-RX-02')
                patient_name = TestDataLoader.generate_patient_name(rx_data['patientNamePrefix'])
                patient_phone = TestDataLoader.generate_patient_phone(rx_data['phonePrefix'])

                await rx_page.create_patient_from_rx(patient_name, rx_data['age'], patient_phone)

                print('Step 3: Verify prescription form is displayed')
                form_visible = await rx_page.verify_prescription_form_displayed()
                assert form_visible, "Prescription form should be displayed"
                print("✓ TC-RX-PAGE-02 PASSED")
            except Exception as e:
                print(f"❌ TC-RX-PAGE-02 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_tc_rx_page_003_add_chief_complaint(self):
        """TC-RX-PAGE-03: Add chief complaint successfully"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                rx_page = PrescriptionPage(page)
                login_data = TestDataLoader.get_login_data()

                print('Step 1: Login to RX page')
                await rx_page.navigate_to_rx_and_login(login_data['username'], login_data['password'])

                print('Step 2: Create patient')
                rx_data = TestDataLoader.get_prescription_data('TC-RX-03')
                patient_name = TestDataLoader.generate_patient_name(rx_data['patientNamePrefix'])
                patient_phone = TestDataLoader.generate_patient_phone(rx_data['phonePrefix'])

                await rx_page.create_patient_from_rx(patient_name, rx_data['age'], patient_phone)

                print('Step 3: Add chief complaint')
                await rx_page.add_chief_complaint(rx_data['chiefComplaint'])

                print('Step 4: Verify chief complaint field is visible')
                field_visible = await rx_page.verify_chief_complaint_field_visible()
                assert field_visible, "Chief complaint field should be visible"
                print("✓ TC-RX-PAGE-03 PASSED")
            except Exception as e:
                print(f"❌ TC-RX-PAGE-03 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_tc_rx_page_004_complete_workflow(self):
        """TC-RX-PAGE-04: Complete prescription workflow"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                rx_page = PrescriptionPage(page)
                login_data = TestDataLoader.get_login_data()

                print('Step 1: Login to RX page')
                await rx_page.navigate_to_rx_and_login(login_data['username'], login_data['password'])

                print('Step 2: Create patient')
                rx_data = TestDataLoader.get_prescription_data('TC-RX-01')
                patient_name = TestDataLoader.generate_patient_name(rx_data['patientNamePrefix'])
                patient_phone = TestDataLoader.generate_patient_phone(rx_data['phonePrefix'])

                await rx_page.create_patient_from_rx(patient_name, rx_data['age'], patient_phone)

                print('Step 3: Add chief complaint')
                await rx_page.add_chief_complaint(rx_data['chiefComplaint'])

                print('Step 4: Save prescription')
                await rx_page.save_prescription()

                print('✓ TC-RX-PAGE-04 PASSED')
            except Exception as e:
                print(f"❌ TC-RX-PAGE-04 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass
