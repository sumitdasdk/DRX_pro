from playwright.async_api import Page
from .BasePage import BasePage


class HistoryPage(BasePage):
    """HistoryPage - Patient history interactions with small focused methods"""

    def __init__(self, page: Page):
        super().__init__(page)

    async def navigate_to_history(self):
        """Navigate to history page"""
        history_button = self.page.get_by_role('button', name='History', exact=True)
        await self.wait_for_element(history_button, 15000)
        await self.click_element(history_button)
        await self.wait(2000)

    async def is_on_history_page(self) -> bool:
        """Check if user is on history page"""
        return 'history' in self.page.url

    async def verify_history_table_displayed(self) -> bool:
        """Verify history table is displayed"""
        table = self.page.locator('table, [class*="table"], [class*="list"]')
        try:
            await table.first.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False

    async def get_history_record_count(self) -> int:
        """Get number of history records displayed"""
        try:
            rows = self.page.locator('tbody tr, [role="row"]')
            count = await rows.count()
            return count
        except:
            return 0

    async def verify_history_records_exist(self) -> bool:
        """Verify history records exist"""
        count = await self.get_history_record_count()
        return count > 0

    async def search_history_by_patient_name(self, patient_name: str):
        """Search history by patient name"""
        search_field = self.page.get_by_role('textbox', name='search|patient')
        try:
            await search_field.wait_for(state='visible', timeout=5000)
            await self.fill_field(search_field, patient_name)
            await self.wait(1000)
        except:
            print('Search field not found, continuing anyway')

    async def get_first_patient_name_from_history(self) -> str:
        """Get first patient name from history"""
        try:
            first_row = self.page.locator('tbody tr, [role="row"]').first
            first_cell = first_row.locator('td, [role="cell"]').first
            text = await first_cell.text_content()
            return text.strip() if text else None
        except:
            return None

    async def verify_patient_exists_in_history(self, patient_name: str) -> bool:
        """Verify patient exists in history"""
        try:
            row = self.page.locator(f'text={patient_name}')
            await row.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False

    async def click_first_history_record(self):
        """Click on first history record"""
        first_row = self.page.locator('tbody tr, [role="row"]').first
        await first_row.wait_for(state='visible', timeout=5000)
        await self.click_element(first_row)
        await self.wait(1000)

    async def get_patient_details_from_history(self) -> dict:
        """Get patient details from history record"""
        try:
            details = {}
            first_row = self.page.locator('tbody tr, [role="row"]').first
            cells = first_row.locator('td, [role="cell"]')
            cell_count = await cells.count()

            if cell_count >= 1:
                details['name'] = await cells.nth(0).text_content()
            if cell_count >= 2:
                details['date'] = await cells.nth(1).text_content()
            if cell_count >= 3:
                details['prescription'] = await cells.nth(2).text_content()

            return details
        except:
            return None

    async def verify_history_page_header_visible(self) -> bool:
        """Verify history page header is visible"""
        header = self.page.locator('h1, h2, [class*="header"], [class*="title"]')
        try:
            await header.first.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False

    async def verify_pagination_controls_exist(self) -> bool:
        """Verify pagination controls exist"""
        pagination = self.page.locator('[class*="pagination"], [class*="pager"]')
        try:
            await pagination.first.wait_for(state='visible', timeout=5000)
            return True
        except:
            return False
