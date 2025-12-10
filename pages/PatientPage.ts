import { Page, Locator, expect } from '@playwright/test';
import { BasePage } from './BasePage';

/**
 * PatientPage contains all selectors and methods related to patient management
 */
export class PatientPage extends BasePage {
  // Selectors for patient list
  private patientsButton: Locator;
  private createPatientButton: Locator;
  private addPatientButton: Locator;
  private searchField: Locator;

  constructor(page: Page) {
    super(page);
    this.patientsButton = page.getByRole('button', { name: 'Patients', exact: true });
    this.createPatientButton = page.getByRole('button', { name: 'Create Patient' });
    this.addPatientButton = page.getByRole('button', { name: 'Add Patient' });
    this.searchField = page.getByRole('textbox', { name: 'search patient' });
  }

  /**
   * Navigate to patients page
   */
  async navigateToPatients() {
    await this.waitForElement(this.patientsButton, 15000);
    await this.clickElement(this.patientsButton);
    await this.waitForURL('**/doctor/patient', 15000);
    await this.wait(2000);
  }

  /**
   * Click Create Patient button
   */
  async clickCreatePatient() {
    await this.waitForElement(this.createPatientButton, 15000);
    await this.clickElement(this.createPatientButton);
    await this.waitForURL('**/doctor/patient/add', 15000);
    await this.wait(1500);
  }

  /**
   * Fill patient creation form
   */
  async fillPatientForm(patientName: string, age: string, phone: string) {
    const nameField = this.page.getByRole('textbox', { name: 'Patient Name' });
    const ageField = this.page.getByRole('textbox', { name: 'Years' });
    const phoneField = this.page.getByRole('textbox', { name: 'e.x: 016********' });

    await this.fillField(nameField, patientName);
    await this.wait(300);

    await this.fillField(ageField, age);
    await this.wait(200);

    await this.fillField(phoneField, phone);
    await this.wait(300);
  }

  /**
   * Submit patient form
   */
  async submitPatientForm() {
    const submitButton = this.page.getByRole('button', { name: 'Submit' });
    await this.waitForElement(submitButton, 5000);
    await this.clickElement(submitButton);
    await this.wait(1000);
  }

  /**
   * Create a new patient
   */
  async createPatient(patientName: string, age: string, phone: string) {
    await this.clickCreatePatient();
    await this.fillPatientForm(patientName, age, phone);
    await this.submitPatientForm();
  }

  /**
   * Search patient by name
   */
  async searchPatientByName(patientName: string) {
    await this.waitForURL('**/doctor/patient', 20000);
    await this.wait(2000);

    await this.fillField(this.searchField, patientName);
    await this.wait(1000);

    const patientRow = this.page.locator(`text=${patientName}`).first();
    await expect(patientRow).toBeVisible({ timeout: 12000 });
  }

  /**
   * Search patient by partial name
   */
  async searchPatientByPartialName(partialName: string, fullPatientName: string) {
    await this.waitForURL('**/doctor/patient', 20000);
    await this.wait(2000);

    await this.fillField(this.searchField, partialName);
    await this.wait(1000);

    const patientRow = this.page.locator(`text=${fullPatientName}`).first();
    await expect(patientRow).toBeVisible({ timeout: 12000 });
  }

  /**
   * Navigate to RX page and try to add patient
   */
  async navigateToRXPage() {
    const rxButton = this.page.getByRole('button', { name: 'RX', exact: true });
    await this.waitForElement(rxButton, 8000);
    await this.clickElement(rxButton);
    await this.waitForURL('**/doctor/rx', 10000);
    await this.wait(2000);
  }

  /**
   * Click Add Patient button (RX page)
   */
  async clickAddPatientFromRX() {
    await this.waitForElement(this.addPatientButton, 30000);
    await this.clickElement(this.addPatientButton);
    await this.wait(600);
  }

  /**
   * Create patient from RX page
   */
  async createPatientFromRX(patientName: string, age: string, phone: string) {
    await this.clickAddPatientFromRX();
    await this.fillPatientForm(patientName, age, phone);
    await this.submitPatientForm();
  }
}
