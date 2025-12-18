from pages_py.BasePage import BasePage


class HistoryPage(BasePage):
    """History Page operations"""

    async def navigate_to_history(self):
        """Navigate to History page"""
        history_button = self.page.get_by_role('button', name='History', exact=True)
        await self.click_element(history_button)

    async def is_on_history_page(self):
        """Check if user is on history page"""
        try:
            await self.page.wait_for_url('**/doctor/history/**', timeout=15000)
            return True
        except:
            return False

    async def verify_history_table_displayed(self):
        """Verify history table is displayed"""
        try:
            table = self.page.locator('table')
            await self.wait_for_element(table, timeout=10000)
            return await table.is_visible()
        except:
            return False

    async def get_history_record_count(self):
        """Get count of history records"""
        try:
            rows = self.page.locator('table tbody tr')
            count = await rows.count()
            return count
        except:
            return 0
