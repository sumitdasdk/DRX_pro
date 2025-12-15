# 🚀 Quick Start Guide - DRX Pro Tests

## ⚡ In 30 Seconds

```bash
# Windows
cd "d:\DRX Pro"
run_tests.bat

# Linux/Mac
cd "d:/DRX Pro"
./run_tests.sh

# Or directly with pytest
python -m pytest tests/ -v
```

---

## ✅ Pre-Flight Checklist

- [ ] Python 3.13.9+ installed: `python --version`
- [ ] Internet connectivity: `ping google.com`
- [ ] Playwright installed: `pip install -r requirements.txt`
- [ ] Working directory: `d:/DRX Pro`

---

## 📊 What's Included

- ✅ **14 Test Cases** ready to execute
- ✅ **4 Test Files** with error handling
- ✅ **5 Page Objects** following POM pattern
- ✅ **Headless Mode** configured
- ✅ **Runner Scripts** for easy execution
- ✅ **Comprehensive Documentation**

---

## 🎯 Test Coverage

| Test File | Tests | IDs |
|-----------|-------|-----|
| test_login.py | 3 | TC-001, TC-002, TC-003 |
| test_patient.py | 3 | TC-P01, TC-P02, TC-P03 |
| test_rxpage.py | 4 | TC-RX-PAGE-01 to 04 |
| test_history.py | 4 | TC-H-PAGE-01 to 04 |

---

## 🔧 Installation (If Needed)

```bash
# Navigate to project
cd "d:/DRX Pro"

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install chromium

# Verify setup
python -m pytest --version
```

---

## 🏃 Run Variations

### Run All Tests
```bash
python -m pytest tests/ -v
```

### Run Specific File
```bash
python -m pytest tests/test_login.py -v
```

### Run Single Test
```bash
python -m pytest tests/test_login.py::TestLogin::test_tc_login_001_user_login_with_valid_credentials -v
```

### Run with Short Output
```bash
python -m pytest tests/ -v --tb=short
```

### Run with Detailed Output
```bash
python -m pytest tests/ -v --tb=long
```

---

## 📈 Expected Results

✅ **Success Output:**
```
tests/test_login.py::TestLogin::test_tc_login_001_user_login_with_valid_credentials PASSED [7%]
✓ TC-001 PASSED: User login successful
...
================================ 14 passed in 45s ================================
```

---

## 🐛 Troubleshooting

### Tests Timeout
**Solution:** Check internet connectivity and server availability
```bash
curl -I http://digital-rx-pro.s3-website-us-east-1.amazonaws.com/
```

### Browser Not Found
**Solution:** Install Playwright browsers
```bash
python -m playwright install chromium
```

### Import Errors
**Solution:** Ensure conftest.py is in tests/ directory
```bash
ls tests/conftest.py  # Should exist
```

---

## 📞 Support

- **Documentation:** See `HEADLESS_MODE_SETUP_COMPLETE.md`
- **Full Report:** See `TEST_EXECUTION_REPORT.md`
- **Summary:** See `TESTING_COMPLETE_SUMMARY.md`
- **GitHub:** https://github.com/sumitdasdk/DRX_pro

---

## ✨ Key Features

✅ Async/await throughout
✅ Headless browser mode
✅ Error handling for connection issues
✅ Clear pass/fail indicators
✅ Independent tests (no dependencies)
✅ Centralized test data
✅ Page Object Model
✅ CI/CD ready

---

**Ready to test?** Just run: `python -m pytest tests/ -v`

🎉 All 14 tests are ready to execute!
