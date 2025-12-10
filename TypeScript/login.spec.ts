import { test, expect } from '@playwright/test';
import { LoginPage } from '../pages/LoginPage';
import { TestDataLoader } from '../pages/TestDataLoader';

test.describe('Digital Rx Pro - Login Tests', () => {
  let loginPage: LoginPage;
  const loginData = TestDataLoader.getLoginData();
  const urls = TestDataLoader.getUrls();

  test.beforeEach(async ({ page }) => {
    loginPage = new LoginPage(page);
    await loginPage.goto(urls.baseUrl);
  });

  test('TC-001: User should successfully login with valid credentials', async () => {
    await loginPage.login(loginData.username, loginData.password);

    expect(loginPage.isLoggedIn()).toBe(true);
  });

  test('TC-002: After login, doctor name should be displayed in top right corner', async () => {
    await loginPage.login(loginData.username, loginData.password);

    const doctorName = await loginPage.getDoctorName();
    expect(doctorName).toContain(loginData.expectedDoctorName);
  });

  test('TC-003: User should be able to navigate to Patient section after login', async ({ page }) => {
    await loginPage.login(loginData.username, loginData.password);

    const patientsButton = page.getByRole('button', { name: 'Patients', exact: true });
    await patientsButton.waitFor({ state: 'visible', timeout: 15000 });
    await patientsButton.click();

    await page.waitForURL(urls.patientPagePattern, { timeout: 15000 });

    expect(page.url()).toContain('doctor/patient');
  });
});
