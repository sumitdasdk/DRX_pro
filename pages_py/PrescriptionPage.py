from playwright.async_api import Page
from .BasePage import BasePage


class PrescriptionPage(BasePage):
    """PrescriptionPage - RX page interactions"""

    def __init__(self, page: Page):
        super().__init__(page)

    async def navigate_to_rx_and_login(self, username: str, password: str):
        """Navigate to RX page and login"""
        await self.goto('http://digital-rx-pro.s3-website-us-east-1.amazonaws.com/')
        
        username_field = self.page.get_by_role('textbox', name='Username')
        password_field = self.page.get_by_role('textbox', name='Password')
        login_button = self.page.get_by_role('button', name='Login')

        await self.fill_field(username_field, username)
        await self.fill_field(password_field, password)
        await self.click_element(login_button)
        await self.page.wait_for_load_state('load', timeout=60000)

    async def is_on_rx_page(self) -> bool:
        """Check if user is on RX page"""
        return 'doctor/rx' in self.page.url

    async def create_patient_from_rx(self, patient_name: str, age: str, phone: str):
        """Create patient from RX page"""
        add_patient_button = self.page.get_by_role('button', name='Add Patient')
        await self.click_element(add_patient_button)

        name_field = self.page.get_by_role('textbox', name='Patient Name')
        age_field = self.page.get_by_role('textbox', name='Years')
        phone_field = self.page.get_by_role('textbox', name='e.x: 016********')
        submit_button = self.page.get_by_role('button', name='Submit')

        await self.fill_field(name_field, patient_name)
        await self.fill_field(age_field, age)
        await self.fill_field(phone_field, phone)
        await self.click_element(submit_button)

    async def add_chief_complaint(self, complaint: str):
        """Add chief complaint"""
        chief_complaint_field = self.page.get_by_role('textbox', name='chief|complaint|symptoms')
        await self.fill_field(chief_complaint_field, complaint)

    async def verify_chief_complaint_field_visible(self) -> bool:
        """Verify chief complaint field is visible"""
        try:
            field = self.page.get_by_role('textbox', name='chief|complaint|symptoms')
            await field.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False

    async def verify_prescription_form_displayed(self) -> bool:
        """Verify prescription form is displayed"""
        try:
            save_btn = self.page.get_by_role('button', name='Save', exact=True)
            await save_btn.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False

    async def save_prescription(self):
        """Save prescription"""
        save_btn = self.page.get_by_role('button', name='Save', exact=True)
        await self.click_element(save_btn)
