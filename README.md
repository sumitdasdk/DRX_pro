# DRX Pro Automation Tests - Python Edition

## Overview
This project contains automated tests for the Digital RX Pro medical application using **Python** with **Playwright** and **pytest**.

## Project Structure
```
.
├── pages_py/                          # Page Object Model classes
│   ├── BasePage.py                   # Base page class with common methods
│   ├── LoginPage.py                  # Login page interactions
│   ├── PatientPage.py                # Patient management interactions
│   ├── PrescriptionPage.py           # Prescription/RX page interactions
│   ├── HistoryPage.py                # History page interactions
│   └── TestDataLoader.py             # Test data manager
├── tests/                             # Test files
│   ├── conftest.py                   # Pytest configuration
│   ├── test_login.py                 # Login test cases (TC-001 to TC-003)
│   ├── test_patient.py               # Patient test cases (TC-P01 to TC-P03)
│   ├── test_rxpage.py                # RX page test cases (TC-RX-PAGE-01 to TC-RX-PAGE-04)
│   └── test_history.py               # History test cases (TC-H-PAGE-01 to TC-H-PAGE-04)
├── test-data/                         # Test data files
│   └── TestData.json                 # Centralized test data
├── pytest.ini                         # Pytest configuration
├── requirements.txt                   # Python dependencies
└── README.md                          # This file

```

## Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup Steps

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Install Playwright browsers:**
   ```bash
   playwright install chromium
   ```

## Running Tests

### Run all tests
```bash
pytest -v
```

### Run specific test file
```bash
pytest tests/test_login.py -v
```

### Run specific test case
```bash
pytest tests/test_login.py::TestLogin::test_tc_login_001_user_login_with_valid_credentials -v
```

### Run tests with output
```bash
pytest -v -s
```

### Run tests by marker
```bash
pytest -v -m asyncio
```

## Test Cases

### Login Tests (TC-001 to TC-003)
- **TC-001:** User login with valid credentials
- **TC-002:** Doctor name is displayed after login
- **TC-003:** Navigation to patient section

### Patient Tests (TC-P01 to TC-P03)
- **TC-P01:** Navigate to patients page
- **TC-P02:** Create a new patient
- **TC-P03:** Search for patient

### RX Page Tests (TC-RX-PAGE-01 to TC-RX-PAGE-04)
- **TC-RX-PAGE-01:** Redirect to RX page after login
- **TC-RX-PAGE-02:** Create patient from RX page
- **TC-RX-PAGE-03:** Add chief complaint
- **TC-RX-PAGE-04:** Complete prescription workflow

### History Tests (TC-H-PAGE-01 to TC-H-PAGE-04)
- **TC-H-PAGE-01:** Navigate to history page
- **TC-H-PAGE-02:** Verify history table displayed
- **TC-H-PAGE-03:** Get history record count
- **TC-H-PAGE-04:** Verify history page header

## Page Object Model (POM)

### BasePage
Base class containing common methods used across all pages:
- `goto()` - Navigate to URL
- `fill_field()` - Fill text field
- `click_element()` - Click element
- `wait()` - Wait milliseconds
- `wait_for_element()` - Wait for element visibility
- `get_text()` - Get element text
- `press_key()` - Press keyboard key
- `wait_for_url()` - Wait for URL pattern

### LoginPage
Handles login functionality:
- `navigate_to_login()` - Navigate to login page
- `login()` - Perform login
- `get_doctor_name()` - Get logged-in doctor name
- `is_logged_in()` - Check if logged in

### PatientPage
Manages patient operations:
- `navigate_to_patients()` - Go to patient page
- `create_patient()` - Create new patient
- `search_patient_by_name()` - Search patients
- `verify_patient_displayed()` - Check patient visibility
- `is_on_patient_page()` - Verify patient page

### PrescriptionPage
Handles prescription/RX operations:
- `navigate_to_rx_and_login()` - Login and go to RX
- `create_patient_from_rx()` - Create patient on RX page
- `add_chief_complaint()` - Add chief complaint
- `save_prescription()` - Save prescription
- `is_on_rx_page()` - Verify RX page

### HistoryPage
Manages history page interactions:
- `navigate_to_history()` - Go to history page
- `verify_history_table_displayed()` - Check table
- `get_history_record_count()` - Get record count
- `search_history_by_patient_name()` - Search history
- `verify_patient_exists_in_history()` - Find patient

## Test Data

Test data is centralized in `test-data/TestData.json`:
- **Login credentials** - Doctor username and password
- **Patient data** - Test patient information (TC-P01 to TC-P07)
- **Prescription data** - RX test data (TC-RX-01 to TC-RX-04)
- **History data** - History test data (TC-H01 to TC-H02)
- **URLs** - Application URL patterns
- **Timeouts** - Default timeout values

## Features

✅ **Page Object Model** - Clean separation of page elements and test logic
✅ **Async/Await** - Modern async Python testing with Playwright
✅ **Centralized Test Data** - JSON-based test data management
✅ **Small Test Cases** - Focused, simple test scenarios
✅ **Pytest Framework** - Industry-standard testing framework
✅ **Cross-browser Ready** - Easy to add Firefox, WebKit testing

## Converting from TypeScript

This project was originally written in TypeScript with Playwright. It has been converted to Python with the following benefits:

- ✅ Simpler syntax
- ✅ Easier maintenance
- ✅ Better for CI/CD pipelines
- ✅ Pythonic code patterns
- ✅ Easier collaboration for Python teams

## Troubleshooting

### Browser connection errors
If you see "Connection closed" errors, ensure:
- Chromium is installed: `playwright install chromium`
- No other Playwright instances are running
- Sufficient system resources

### Import errors
If you see import errors:
- Ensure you're in the project root directory
- Python path should automatically include parent directories via conftest.py
- Check that pages_py and tests folders exist

### Test timeouts
If tests timeout:
- Check application server is accessible
- Increase timeout values in pytest.ini
- Check network connectivity

## Future Enhancements

- [ ] Add Firefox and WebKit browsers
- [ ] Add screenshot on failure
- [ ] Add HTML report generation
- [ ] Add email test reports
- [ ] Add performance testing
- [ ] Add API testing integration
- [ ] Add mobile device testing

## License

This project is for internal use only.

## Support

For issues or questions, please contact the QA team.
