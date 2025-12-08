import { test, expect } from '@playwright/test';

test.describe('Digital Rx Pro - Login Tests', () => {
  test.beforeEach(async ({ page }) => {
    // Navigate to the application
    await page.goto('http://digital-rx-pro.s3-website-us-east-1.amazonaws.com/', { waitUntil: 'domcontentloaded', timeout: 90000 });
  });

  test('TC-001: User should successfully login with valid credentials', async ({ page }) => {
    // Arrange - Get username and password fields
    const usernameField = page.getByRole('textbox', { name: 'Username' });
    const passwordField = page.getByRole('textbox', { name: 'Password' });
    const loginButton = page.getByRole('button', { name: 'Login' });

    // Act - Fill in login credentials
    await usernameField.fill('Sadman');
    await passwordField.fill('Sadman1#');

    // Click the Login button and wait for navigation
    await Promise.all([
      page.waitForURL('**/doctor/rx', { timeout: 30000 }),
      loginButton.click()
    ]);

    // Assert - Verify URL contains 'doctor/rx'
    expect(page.url()).toContain('doctor/rx');
  });

  test('TC-002: After login, doctor name should be displayed in top right corner', async ({ page }) => {
    // Arrange - Get username and password fields
    const usernameField = page.getByRole('textbox', { name: 'Username' });
    const passwordField = page.getByRole('textbox', { name: 'Password' });
    const loginButton = page.getByRole('button', { name: 'Login' });

    // Act - Fill in login credentials and login
    await usernameField.fill('Sadman');
    await passwordField.fill('Sadman1#');

    // Click login and wait for navigation
    await Promise.all([
      page.waitForURL('**/doctor/rx', { timeout: 30000 }),
      loginButton.click()
    ]);

    // Assert - Verify doctor name is displayed in top right corner
    // Use a more specific selector that targets the User button's paragraph element
    const doctorNameInButton = page.getByRole('button', { name: 'User' }).first().locator('p');
    await expect(doctorNameInButton).toContainText('Dr. Sadman Soeb Adib', { timeout: 10000 });

    // Additional assertion - Verify URL contains doctor/rx
    expect(page.url()).toContain('doctor/rx');
  });

  test('TC-003: User should be able to navigate to Patient section after login', async ({ page }) => {
    // Arrange - Login first
    const usernameField = page.getByRole('textbox', { name: 'Username' });
    const passwordField = page.getByRole('textbox', { name: 'Password' });
    const loginButton = page.getByRole('button', { name: 'Login' });

    // Act - Fill in login credentials and login
    await usernameField.fill('Sadman');
    await passwordField.fill('Sadman1#');

    // Click login and wait for navigation
    await Promise.all([
      page.waitForURL('**/doctor/rx', { timeout: 30000 }),
      loginButton.click()
    ]);

    // Click on Patients button
    const patientsButton = page.getByRole('button', { name: 'Patients', exact: true });
    await patientsButton.click();

    // Wait for patient page to load
    await page.waitForURL('**/doctor/patient', { timeout: 15000 });

    // Assert - Verify URL contains 'doctor/patient'
    expect(page.url()).toContain('doctor/patient');

    // Verify Create Patient button is visible
    const createPatientButton = page.getByRole('button', { name: 'Create Patient' });
    await expect(createPatientButton).toBeVisible();
  });
});
