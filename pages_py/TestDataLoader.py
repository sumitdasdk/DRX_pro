import json
import os
from datetime import datetime
from pathlib import Path


class TestDataLoader:
    """Helper class to load and access test data from JSON file"""

    test_data = None

    @staticmethod
    def load_test_data():
        """Load test data from TestData.json"""
        if TestDataLoader.test_data is None:
            # Get the directory of this file
            current_dir = Path(__file__).parent.parent
            test_data_path = current_dir / 'test-data' / 'TestData.json'

            with open(test_data_path, 'r', encoding='utf-8') as f:
                TestDataLoader.test_data = json.load(f)

        return TestDataLoader.test_data

    @staticmethod
    def get_login_data():
        """Get login credentials"""
        return TestDataLoader.load_test_data()['login']

    @staticmethod
    def get_patient_data(test_case_id: str):
        """Get patient test data for a specific test case"""
        return TestDataLoader.load_test_data()['patient'].get(test_case_id)

    @staticmethod
    def get_prescription_data(test_case_id: str):
        """Get prescription test data for a specific test case"""
        return TestDataLoader.load_test_data()['prescription'].get(test_case_id)

    @staticmethod
    def get_history_data(test_case_id: str):
        """Get history test data for a specific test case"""
        return TestDataLoader.load_test_data()['history'].get(test_case_id)

    @staticmethod
    def get_urls():
        """Get URL patterns"""
        return TestDataLoader.load_test_data()['urls']

    @staticmethod
    def get_timeouts():
        """Get timeout values"""
        return TestDataLoader.load_test_data()['timeouts']

    @staticmethod
    def generate_patient_name(prefix: str) -> str:
        """Generate unique patient name with timestamp"""
        timestamp = datetime.now().strftime('%H%M%S')
        return f"{prefix}_{timestamp}"

    @staticmethod
    def generate_patient_phone(phone_prefix: str) -> str:
        """Generate unique patient phone with timestamp"""
        timestamp = datetime.now().strftime('%H%M%S')
        # Take first 8 digits of prefix and add last 4 digits of timestamp
        return f"{phone_prefix}{timestamp[-4:]}"
