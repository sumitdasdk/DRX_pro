from playwright.async_api import Page
from .BasePage import BasePage


class LoginPage(BasePage):
    """LoginPage contains all selectors and methods related to login functionality"""

    def __init__(self, page: Page):
        super().__init__(page)

    async def navigate_to_login(self):
        """Navigate to login page"""
        await self.goto('http://digital-rx-pro.s3-website-us-east-1.amazonaws.com/')
        await self.wait(1000)

    async def login(self, username: str, password: str):
        """Perform login with credentials"""
        username_field = self.page.get_by_role('textbox', name='Username')
        password_field = self.page.get_by_role('textbox', name='Password')
        login_button = self.page.get_by_role('button', name='Login')

        await self.fill_field(username_field, username)
        await self.fill_field(password_field, password)

        # Wait for navigation while clicking login
        async with self.page.expect_navigation(wait_until='domcontentloaded', timeout=90000):
            await self.click_element(login_button)

        await self.wait(3000)

    async def get_doctor_name(self) -> str:
        """Get doctor name from top right button"""
        doctor_button = self.page.locator('[class*="user"], [class*="profile"], button').filter(has_text='Dr')
        return await doctor_button.first.text_content()

    async def is_logged_in(self) -> bool:
        """Check if user is logged in"""
        return 'doctor/rx' in self.page.url or 'doctor/patient' in self.page.url
