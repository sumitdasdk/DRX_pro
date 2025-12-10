import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

/**
 * PrescriptionPage - Simple version for basic prescription writing
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
   * Create patient from RX page
   */
  async createPatientFromRX(patientName: string, age: string, phone: string) {
    const addPatientButton = this.page.getByRole('button', { name: 'Add Patient' });
    
    // Wait for Add Patient button with longer timeout
    await addPatientButton.waitFor({ state: 'visible', timeout: 60000 });
    await this.clickElement(addPatientButton);
    await this.wait(800);

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
   * Save prescription
   */
  async savePrescription() {
    const saveBtn = this.page.getByRole('button', { name: 'Save', exact: true });
    await this.waitForElement(saveBtn, 15000);
    await this.clickElement(saveBtn);
    await this.wait(1000);
  }
}

