from playwright.async_api import Page
from .BasePage import BasePage


class PrescriptionPage(BasePage):
    """PrescriptionPage - RX page interactions with small focused methods"""

    def __init__(self, page: Page):
        super().__init__(page)

    async def navigate_to_rx_and_login(self, username: str, password: str):
        """Navigate to RX page and login"""
        username_field = self.page.get_by_role('textbox', name='Username')
        password_field = self.page.get_by_role('textbox', name='Password')
        login_button = self.page.get_by_role('button', name='Login')

        await self.goto('http://digital-rx-pro.s3-website-us-east-1.amazonaws.com/')
        await self.fill_field(username_field, username)
        await self.fill_field(password_field, password)

        async with self.page.expect_navigation(wait_until='domcontentloaded', timeout=90000):
            await self.click_element(login_button)

        await self.wait(3000)

    async def is_on_rx_page(self) -> bool:
        """Check if user is on RX page"""
        return 'doctor/rx' in self.page.url

    def get_add_patient_button(self):
        """Get Add Patient button"""
        return self.page.get_by_role('button', name='Add Patient')

    async def verify_add_patient_button_visible(self) -> bool:
        """Verify Add Patient button is visible"""
        button = self.get_add_patient_button()
        try:
            await button.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False

    async def click_add_patient_button(self):
        """Click Add Patient button"""
        button = self.get_add_patient_button()
        await button.wait_for(state='visible', timeout=60000)
        await self.click_element(button)
        await self.wait(800)

    async def create_patient_from_rx(self, patient_name: str, age: str, phone: str):
        """Create patient from RX page"""
        await self.click_add_patient_button()

        name_field = self.page.get_by_role('textbox', name='Patient Name')
        age_field = self.page.get_by_role('textbox', name='Years')
        phone_field = self.page.get_by_role('textbox', name='e.x: 016********')
        submit_button = self.page.get_by_role('button', name='Submit')

        await self.fill_field(name_field, patient_name)
        await self.wait(300)
        await self.fill_field(age_field, age)
        await self.wait(200)
        await self.fill_field(phone_field, phone)
        await self.wait(300)
        await self.click_element(submit_button)
        await self.wait(1000)

    async def add_chief_complaint(self, complaint: str):
        """Add chief complaint"""
        chief_complaint_field = self.page.get_by_role('textbox', name='chief|complaint|symptoms')
        await self.fill_field(chief_complaint_field, complaint)
        await self.wait(500)

    def get_chief_complaint_field(self):
        """Get chief complaint field"""
        return self.page.get_by_role('textbox', name='chief|complaint|symptoms')

    async def verify_chief_complaint_field_visible(self) -> bool:
        """Verify chief complaint field is visible"""
        field = self.get_chief_complaint_field()
        try:
            await field.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False

    def get_save_button(self):
        """Get Save button"""
        return self.page.get_by_role('button', name='Save', exact=True)

    async def verify_save_button_visible(self) -> bool:
        """Verify Save button is visible"""
        button = self.get_save_button()
        try:
            await button.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False

    async def save_prescription(self):
        """Save prescription"""
        save_btn = self.get_save_button()
        await self.wait_for_element(save_btn, 15000)
        await self.click_element(save_btn)
        await self.wait(1000)

    async def verify_prescription_form_displayed(self) -> bool:
        """Verify prescription form is displayed"""
        save_btn = self.get_save_button()
        try:
            await save_btn.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False
