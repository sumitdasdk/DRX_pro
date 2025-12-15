from playwright.async_api import Page
from .BasePage import BasePage


class PatientPage(BasePage):
    """PatientPage contains all methods related to patient management"""

    def __init__(self, page: Page):
        super().__init__(page)

    async def navigate_to_patients(self):
        """Navigate to Patients page"""
        patients_button = self.page.get_by_role('button', name='Patients', exact=True)
        await self.wait_for_element(patients_button, 15000)
        await self.click_element(patients_button)
        await self.wait(2000)

    async def create_patient(self, name: str, age: str, phone: str):
        """Create a new patient"""
        add_patient_button = self.page.get_by_role('button', name='Add Patient')
        await self.click_element(add_patient_button)
        await self.wait(500)

        name_field = self.page.get_by_role('textbox', name='Patient Name')
        age_field = self.page.get_by_role('textbox', name='Years')
        phone_field = self.page.get_by_role('textbox', name='e.x: 016********')
        submit_button = self.page.get_by_role('button', name='Submit')

        await self.fill_field(name_field, name)
        await self.wait(300)
        await self.fill_field(age_field, age)
        await self.wait(200)
        await self.fill_field(phone_field, phone)
        await self.wait(300)
        await self.click_element(submit_button)
        await self.wait(1000)

    async def search_patient_by_name(self, name: str):
        """Search for patient by name"""
        search_field = self.page.get_by_role('textbox', name='Search')
        await self.fill_field(search_field, name)
        await self.wait(1000)

    async def verify_patient_displayed(self, name: str) -> bool:
        """Verify patient is displayed in list"""
        try:
            patient_row = self.page.locator(f'text={name}')
            await patient_row.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False

    async def is_on_patient_page(self) -> bool:
        """Check if user is on patient page"""
        return 'doctor/patient' in self.page.url
