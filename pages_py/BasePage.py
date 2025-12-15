from playwright.async_api import Page, Locator
import asyncio

class BasePage:
    """BasePage class contains common actions that can be used across all page objects"""

    def __init__(self, page: Page):
        self.page = page

    async def goto(self, url: str):
        """Navigate to a URL"""
        await self.page.goto(url, wait_until='domcontentloaded', timeout=90000)

    async def fill_field(self, locator: Locator, value: str):
        """Fill a text field with value"""
        await locator.wait_for(state='visible', timeout=10000)
        await locator.fill(value)

    async def click_element(self, locator: Locator):
        """Click an element"""
        await locator.wait_for(state='visible', timeout=15000)
        await locator.click()

    async def wait_for_element(self, locator: Locator, timeout: int = 10000):
        """Wait for element to be visible"""
        await locator.wait_for(state='visible', timeout=timeout)

    async def wait(self, milliseconds: int):
        """Wait for specified milliseconds"""
        await asyncio.sleep(milliseconds / 1000)

    async def get_text(self, locator: Locator) -> str:
        """Get text content from element"""
        return await locator.text_content()

    async def press_key(self, key: str):
        """Press a keyboard key"""
        await self.page.keyboard.press(key)

    async def wait_for_url(self, url_pattern: str, timeout: int = 30000):
        """Wait for URL to match pattern"""
        await self.page.wait_for_url(url_pattern, timeout=timeout)

    async def evaluate(self, script: str):
        """Evaluate JavaScript"""
        return await self.page.evaluate(script)
