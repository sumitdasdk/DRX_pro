import pytest
import sys
from pathlib import Path
from playwright.async_api import async_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from pages_py.LoginPage import LoginPage
from pages_py.PatientPage import PatientPage
from pages_py.TestDataLoader import TestDataLoader


class TestPatient:
    """Patient test cases"""

    async def _login_and_navigate_to_patients(self, page):
        """Helper to login and navigate to patients page"""
        login_page = LoginPage(page)
        login_data = TestDataLoader.get_login_data()
        urls = TestDataLoader.get_urls()

        await page.goto(urls['baseUrl'])
        await login_page.login(login_data['username'], login_data['password'])
        
        patient_page = PatientPage(page)
        await patient_page.navigate_to_patients()
        return patient_page

    @pytest.mark.asyncio
    async def test_tc_patient_001_navigate_to_patients(self):
        """TC-P01: User should navigate to Patients page"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                patient_page = await self._login_and_navigate_to_patients(page)
                assert await patient_page.is_on_patient_page(), "User should be on patient page"
                print("✓ TC-P01 PASSED: Navigate to patients page")
            except Exception as e:
                print(f"❌ TC-P01 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_tc_patient_002_create_patient(self):
        """TC-P02: User should be able to create a patient"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                patient_page = await self._login_and_navigate_to_patients(page)
                
                patient_data = TestDataLoader.get_patient_data('TC-P01')
                patient_name = TestDataLoader.generate_patient_name(patient_data['name'])
                patient_phone = TestDataLoader.generate_patient_phone(patient_data['phonePrefix'])

                await patient_page.create_patient(patient_name, patient_data['age'], patient_phone)

                patient_displayed = await patient_page.verify_patient_displayed(patient_name)
                assert patient_displayed, f"Patient {patient_name} should be displayed"
                print("✓ TC-P02 PASSED: Create patient")
            except Exception as e:
                print(f"❌ TC-P02 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass

    @pytest.mark.asyncio
    async def test_tc_patient_003_search_patient(self):
        """TC-P03: User should be able to search for patient"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                patient_page = await self._login_and_navigate_to_patients(page)

                patient_data = TestDataLoader.get_patient_data('TC-P02')
                patient_name = TestDataLoader.generate_patient_name(patient_data['name'])
                patient_phone = TestDataLoader.generate_patient_phone(patient_data['phonePrefix'])

                await patient_page.create_patient(patient_name, patient_data['age'], patient_phone)
                await patient_page.search_patient_by_name(patient_name)

                patient_found = await patient_page.verify_patient_displayed(patient_name)
                assert patient_found, f"Patient {patient_name} should be found in search"
                print("✓ TC-P03 PASSED: Search patient")
            except Exception as e:
                print(f"❌ TC-P03 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass
