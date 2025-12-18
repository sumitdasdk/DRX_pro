from playwright.async_api import Page, Locator


class BasePage:
    """BasePage class contains common actions"""

    def __init__(self, page: Page):
        self.page = page

    async def goto(self, url: str):
        """Navigate to a URL"""
        await self.page.goto(url, wait_until='domcontentloaded')

    async def fill_field(self, locator: Locator, value: str):
        """Fill a text field"""
        await locator.fill(value)

    async def click_element(self, locator: Locator):
        """Click an element"""
        await locator.click()

    async def wait_for_element(self, locator: Locator, timeout: int = 5000):
        """Wait for element to be visible"""
        await locator.wait_for(state='visible', timeout=timeout)
