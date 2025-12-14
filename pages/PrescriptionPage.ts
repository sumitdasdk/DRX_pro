import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

/**
 * PrescriptionPage - RX page interactions with small focused methods
 */
export class PrescriptionPage extends BasePage {
  constructor(page: Page) {
    super(page);
  }

  /**
   * Navigate to RX page and login
   */
  async navigateToRXAndLogin(username: string, password: string) {
    const usernameField = this.page.getByRole('textbox', { name: 'Username' });
    const passwordField = this.page.getByRole('textbox', { name: 'Password' });
    const loginButton = this.page.getByRole('button', { name: 'Login' });

    await this.goto('http://digital-rx-pro.s3-website-us-east-1.amazonaws.com/');

    await this.fillField(usernameField, username);
    await this.fillField(passwordField, password);

    // Wait for navigation and click login
    await Promise.all([
      this.page.waitForNavigation({ waitUntil: 'domcontentloaded', timeout: 90000 }),
      this.clickElement(loginButton)
    ]);
    
    await this.wait(3000);
  }

  /**
   * Check if user is on RX page (doctor/rx URL)
   */
  async isOnRXPage(): Promise<boolean> {
    return this.page.url().includes('doctor/rx');
  }

  /**
   * Get Add Patient button
   */
  private getAddPatientButton(): Locator {
    return this.page.getByRole('button', { name: 'Add Patient' });
  }

  /**
   * Verify Add Patient button is visible
   */
  async verifyAddPatientButtonVisible(): Promise<boolean> {
    const button = this.getAddPatientButton();
    try {
      await button.waitFor({ state: 'visible', timeout: 10000 });
      return true;
    } catch {
      return false;
    }
  }

  /**
   * Click Add Patient button
   */
  async clickAddPatientButton() {
    const button = this.getAddPatientButton();
    await button.waitFor({ state: 'visible', timeout: 60000 });
    await this.clickElement(button);
    await this.wait(800);
  }

  /**
   * Create patient from RX page
   */
  async createPatientFromRX(patientName: string, age: string, phone: string) {
    await this.clickAddPatientButton();

    const nameField = this.page.getByRole('textbox', { name: 'Patient Name' });
    const ageField = this.page.getByRole('textbox', { name: 'Years' });
    const phoneField = this.page.getByRole('textbox', { name: 'e.x: 016********' });
    const submitButton = this.page.getByRole('button', { name: 'Submit' });

    await this.fillField(nameField, patientName);
    await this.wait(300);

    await this.fillField(ageField, age);
    await this.wait(200);

    await this.fillField(phoneField, phone);
    await this.wait(300);

    await this.clickElement(submitButton);
    await this.wait(1000);
  }

  /**
   * Add chief complaint
   */
  async addChiefComplaint(complaint: string) {
    const chiefComplaintField = this.page.getByRole('textbox', { name: /chief|complaint|symptoms/i });
    await this.fillField(chiefComplaintField, complaint);
    await this.wait(500);
  }

  /**
   * Get chief complaint field
   */
  private getChiefComplaintField(): Locator {
    return this.page.getByRole('textbox', { name: /chief|complaint|symptoms/i });
  }

  /**
   * Verify chief complaint field is visible
   */
  async verifyChiefComplaintFieldVisible(): Promise<boolean> {
    const field = this.getChiefComplaintField();
    try {
      await field.waitFor({ state: 'visible', timeout: 10000 });
      return true;
    } catch {
      return false;
    }
  }

  /**
   * Get Save button
   */
  private getSaveButton(): Locator {
    return this.page.getByRole('button', { name: 'Save', exact: true });
  }

  /**
   * Verify Save button is visible
   */
  async verifySaveButtonVisible(): Promise<boolean> {
    const button = this.getSaveButton();
    try {
      await button.waitFor({ state: 'visible', timeout: 10000 });
      return true;
    } catch {
      return false;
    }
  }

  /**
   * Save prescription
   */
  async savePrescription() {
    const saveBtn = this.getSaveButton();
    await this.waitForElement(saveBtn, 15000);
    await this.clickElement(saveBtn);
    await this.wait(1000);
  }

  /**
   * Get prescription form title/header text
   */
  async getPrescriptionFormTitle(): Promise<string | null> {
    try {
      const title = await this.page.locator('h1, h2, .form-title, [class*="title"]').first().textContent();
      return title?.trim() || null;
    } catch {
      return null;
    }
  }

  /**
   * Verify prescription form is displayed
   */
  async verifyPrescriptionFormDisplayed(): Promise<boolean> {
    const saveBtn = this.getSaveButton();
    try {
      await saveBtn.waitFor({ state: 'visible', timeout: 10000 });
      return true;
    } catch {
      return false;
    }
  }
}

