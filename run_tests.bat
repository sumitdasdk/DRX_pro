@echo off
REM DRX Pro Test Suite Runner - Headless Mode (Windows)
REM This batch script runs all tests in headless mode with comprehensive reporting

echo.
echo ==========================================
echo DRX Pro - Test Suite Execution (Headless)
echo ==========================================
echo.

cd /d "d:\DRX Pro"

echo 📊 Test Environment Information:
python --version
python -m pytest --version
echo.

echo 🚀 Starting Test Execution...
echo.
echo Configuration:
echo   - Mode: Headless (browser UI not displayed^)
echo   - Framework: pytest 8.4.1 with pytest-asyncio 1.3.0
echo   - Total Tests: 14 test cases
echo   - Architecture: Page Object Model (POM^)
echo.

echo Test Files:
echo   * test_login.py (3 tests: TC-001, TC-002, TC-003^)
echo   * test_patient.py (3 tests: TC-P01, TC-P02, TC-P03^)
echo   * test_rxpage.py (4 tests: TC-RX-PAGE-01 to 04^)
echo   * test_history.py (4 tests: TC-H-PAGE-01 to 04^)
echo.

for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a:%%b)
echo ⏱️  Starting test run at: %mydate% %mytime%
echo ==========================================
echo.

REM Run tests with verbose output
python -m pytest tests/ -v --tb=short

REM Capture exit code
set TEST_EXIT_CODE=%ERRORLEVEL%

echo.
echo ==========================================
echo Test Execution Complete
echo ==========================================
echo.

if %TEST_EXIT_CODE% equ 0 (
    echo ✅ ALL TESTS PASSED!
) else (
    echo ⚠️  Some tests failed. Exit code: %TEST_EXIT_CODE%
    echo.
    echo Common Issues:
    echo   1. Network: Verify internet connectivity
    echo   2. Server: Check if http://digital-rx-pro.s3-website-us-east-1.amazonaws.com/ is accessible
    echo   3. Browser: Reinstall browsers with: python -m playwright install chromium
    echo   4. Timeout: Increase timeout in TestData.json if server is slow
)

echo.
for /f "tokens=2-4 delims=/ " %%a in ('date /t') do (set mydate=%%c-%%a-%%b)
for /f "tokens=1-2 delims=/:" %%a in ('time /t') do (set mytime=%%a:%%b)
echo ⏱️  Test execution ended at: %mydate% %mytime%
echo.

exit /b %TEST_EXIT_CODE%
