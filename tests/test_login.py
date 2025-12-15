import pytest
import sys
from pathlib import Path
from playwright.async_api import async_playwright

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from pages_py.LoginPage import LoginPage
from pages_py.TestDataLoader import TestDataLoader


class TestLogin:
    """Login test cases"""

    @pytest.mark.asyncio
    async def test_tc_login_001_user_login_with_valid_credentials(self):
        """TC-001: User should successfully login with valid credentials"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                login_page = LoginPage(page)
                login_data = TestDataLoader.get_login_data()
                urls = TestDataLoader.get_urls()

                await page.goto(urls['baseUrl'])
                await login_page.login(login_data['username'], login_data['password'])

                assert await login_page.is_logged_in(), "User should be logged in"
                print("✓ TC-001 PASSED: User login successful")
            except Exception as e:
                print(f"❌ TC-001 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass  # Browser already closed or connection lost

    @pytest.mark.asyncio
    async def test_tc_login_002_doctor_name_displayed(self):
        """TC-002: After login, doctor name should be displayed"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                login_page = LoginPage(page)
                login_data = TestDataLoader.get_login_data()
                urls = TestDataLoader.get_urls()

                await page.goto(urls['baseUrl'])
                await login_page.login(login_data['username'], login_data['password'])

                doctor_name = await login_page.get_doctor_name()
                assert login_data['expectedDoctorName'] in doctor_name, f"Doctor name should contain {login_data['expectedDoctorName']}"
                print("✓ TC-002 PASSED: Doctor name displayed")
            except Exception as e:
                print(f"❌ TC-002 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass  # Browser already closed or connection lost

    @pytest.mark.asyncio
    async def test_tc_login_003_navigate_to_patient_section(self):
        """TC-003: User should be able to navigate to Patient section"""
        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            page = await browser.new_page()
            try:
                login_page = LoginPage(page)
                login_data = TestDataLoader.get_login_data()
                urls = TestDataLoader.get_urls()

                await page.goto(urls['baseUrl'])
                await login_page.login(login_data['username'], login_data['password'])

                patients_button = page.get_by_role('button', name='Patients', exact=True)
                await patients_button.wait_for(state='visible', timeout=15000)
                await patients_button.click()

                await page.wait_for_url(urls['patientPagePattern'], timeout=15000)

                assert 'doctor/patient' in page.url, "User should be on patient page"
                print("✓ TC-003 PASSED: Navigate to patient section")
            except Exception as e:
                print(f"❌ TC-003 FAILED: {str(e)}")
                raise
            finally:
                try:
                    await browser.close()
                except Exception:
                    pass  # Browser already closed or connection lost
