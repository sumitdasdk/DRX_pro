import pytest
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from playwright.async_api import async_playwright
from pages_py.LoginPage import LoginPage
from pages_py.PatientPage import PatientPage
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


class TestPatient:
    """Patient test cases"""

    @pytest.mark.asyncio
    async def test_tc_patient_001_navigate_to_patients(self, authenticated_page):
        """TC-P01: User should navigate to Patients page"""
        page = authenticated_page
        patient_page = PatientPage(page)

        print('Step 1: Navigate to Patients page')
        await patient_page.navigate_to_patients()

        print('Step 2: Verify user is on patient page')
        assert await patient_page.is_on_patient_page(), "User should be on patient page"

    @pytest.mark.asyncio
    async def test_tc_patient_002_create_patient(self, authenticated_page):
        """TC-P02: User should be able to create a patient"""
        page = authenticated_page
        patient_page = PatientPage(page)

        print('Step 1: Navigate to Patients page')
        await patient_page.navigate_to_patients()

        print('Step 2: Create patient')
        patient_data = TestDataLoader.get_patient_data('TC-P01')
        patient_name = TestDataLoader.generate_patient_name(patient_data['name'])
        patient_phone = TestDataLoader.generate_patient_phone(patient_data['phonePrefix'])

        await patient_page.create_patient(patient_name, patient_data['age'], patient_phone)

        print('Step 3: Verify patient is displayed')
        patient_displayed = await patient_page.verify_patient_displayed(patient_name)
        assert patient_displayed, f"Patient {patient_name} should be displayed"

    @pytest.mark.asyncio
    async def test_tc_patient_003_search_patient(self, authenticated_page):
        """TC-P03: User should be able to search for patient"""
        page = authenticated_page
        patient_page = PatientPage(page)

        print('Step 1: Navigate to Patients page')
        await patient_page.navigate_to_patients()

        print('Step 2: Create patient')
        patient_data = TestDataLoader.get_patient_data('TC-P02')
        patient_name = TestDataLoader.generate_patient_name(patient_data['name'])
        patient_phone = TestDataLoader.generate_patient_phone(patient_data['phonePrefix'])

        await patient_page.create_patient(patient_name, patient_data['age'], patient_phone)

        print('Step 3: Search for patient')
        await patient_page.search_patient_by_name(patient_name)

        print('Step 4: Verify patient is found')
        patient_found = await patient_page.verify_patient_displayed(patient_name)
        assert patient_found, f"Patient {patient_name} should be found in search"
