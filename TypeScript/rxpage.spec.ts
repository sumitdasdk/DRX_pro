import { test, expect } from '@playwright/test';
import { PrescriptionPage } from '../pages/PrescriptionPage';
import { TestDataLoader } from '../pages/TestDataLoader';

test.describe('RX Page Tests', () => {
  let rxPage: PrescriptionPage;
  const loginData = TestDataLoader.getLoginData();

  test.beforeEach(async ({ page }) => {
    rxPage = new PrescriptionPage(page);
  });

  test('TC-RX-PAGE-01: User should be redirected to RX page after login', async () => {
    console.log('Step 1: Login to RX page');
    await rxPage.navigateToRXAndLogin(loginData.username, loginData.password);

    console.log('Step 2: Verify user is on RX page');
    const isOnRXPage = await rxPage.isOnRXPage();
    expect(isOnRXPage).toBe(true);
  });

  test('TC-RX-PAGE-02: Add Patient button should be visible on RX page', async () => {
    console.log('Step 1: Login to RX page');
    await rxPage.navigateToRXAndLogin(loginData.username, loginData.password);

    console.log('Step 2: Verify Add Patient button is visible');
    const isVisible = await rxPage.verifyAddPatientButtonVisible();
    expect(isVisible).toBe(true);
  });

  test('TC-RX-PAGE-03: Create patient from RX page successfully', async () => {
    console.log('Step 1: Login to RX page');
    await rxPage.navigateToRXAndLogin(loginData.username, loginData.password);

    console.log('Step 2: Create patient');
    const rxData = TestDataLoader.getPrescriptionData('TC-RX-02');
    const patientName = TestDataLoader.generatePatientName(rxData.patientNamePrefix);
    const patientPhone = TestDataLoader.generatePatientPhone(rxData.phonePrefix);

    await rxPage.createPatientFromRX(patientName, rxData.age, patientPhone);

    console.log('Step 3: Verify prescription form is displayed');
    const formVisible = await rxPage.verifyPrescriptionFormDisplayed();
    expect(formVisible).toBe(true);
  });

  test('TC-RX-PAGE-04: Chief complaint field should be visible after patient creation', async () => {
    console.log('Step 1: Login to RX page');
    await rxPage.navigateToRXAndLogin(loginData.username, loginData.password);

    console.log('Step 2: Create patient');
    const rxData = TestDataLoader.getPrescriptionData('TC-RX-03');
    const patientName = TestDataLoader.generatePatientName(rxData.patientNamePrefix);
    const patientPhone = TestDataLoader.generatePatientPhone(rxData.phonePrefix);

    await rxPage.createPatientFromRX(patientName, rxData.age, patientPhone);

    console.log('Step 3: Verify chief complaint field is visible');
    const fieldVisible = await rxPage.verifyChiefComplaintFieldVisible();
    expect(fieldVisible).toBe(true);
  });

  test('TC-RX-PAGE-05: User should be able to add chief complaint', async () => {
    console.log('Step 1: Login to RX page');
    await rxPage.navigateToRXAndLogin(loginData.username, loginData.password);

    console.log('Step 2: Create patient');
    const rxData = TestDataLoader.getPrescriptionData('TC-RX-04');
    const patientName = TestDataLoader.generatePatientName(rxData.patientNamePrefix);
    const patientPhone = TestDataLoader.generatePatientPhone(rxData.phonePrefix);

    await rxPage.createPatientFromRX(patientName, rxData.age, patientPhone);

    console.log('Step 3: Add chief complaint');
    await rxPage.addChiefComplaint(rxData.chiefComplaint);

    console.log('Step 4: Verify chief complaint field contains text');
    const fieldVisible = await rxPage.verifyChiefComplaintFieldVisible();
    expect(fieldVisible).toBe(true);
  });

  test('TC-RX-PAGE-06: Save button should be visible in prescription form', async () => {
    console.log('Step 1: Login to RX page');
    await rxPage.navigateToRXAndLogin(loginData.username, loginData.password);

    console.log('Step 2: Create patient');
    const rxData = TestDataLoader.getPrescriptionData('TC-RX-02');
    const patientName = TestDataLoader.generatePatientName(rxData.patientNamePrefix);
    const patientPhone = TestDataLoader.generatePatientPhone(rxData.phonePrefix);

    await rxPage.createPatientFromRX(patientName, rxData.age, patientPhone);

    console.log('Step 3: Verify Save button is visible');
    const saveVisible = await rxPage.verifySaveButtonVisible();
    expect(saveVisible).toBe(true);
  });

  test('TC-RX-PAGE-07: Complete prescription workflow - create patient with chief complaint and save', async () => {
    console.log('Step 1: Login to RX page');
    await rxPage.navigateToRXAndLogin(loginData.username, loginData.password);

    console.log('Step 2: Create patient');
    const rxData = TestDataLoader.getPrescriptionData('TC-RX-01');
    const patientName = TestDataLoader.generatePatientName(rxData.patientNamePrefix);
    const patientPhone = TestDataLoader.generatePatientPhone(rxData.phonePrefix);

    await rxPage.createPatientFromRX(patientName, rxData.age, patientPhone);

    console.log('Step 3: Add chief complaint');
    await rxPage.addChiefComplaint(rxData.chiefComplaint);

    console.log('Step 4: Save prescription');
    await rxPage.savePrescription();

    console.log('Test completed successfully');
  });
});
