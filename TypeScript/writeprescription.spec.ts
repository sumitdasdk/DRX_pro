import { test, expect } from '@playwright/test';
import { PrescriptionPage } from '../pages/PrescriptionPage';
import { TestDataLoader } from '../pages/TestDataLoader';

test.describe('Prescription Writing Tests', () => {
  test('TC-RX-01: Simple prescription workflow - Login > Create Patient > Add Chief Complaint > Save', async ({ page }) => {
    const prescriptionPage = new PrescriptionPage(page);

    // Load test data
    const loginData = TestDataLoader.getLoginData();
    const rxData = TestDataLoader.getPrescriptionData('TC-RX-01');

    // Step 1: Navigate to RX and login
    console.log('Step 1: Logging in to RX page...');
    await prescriptionPage.navigateToRXAndLogin(loginData.username, loginData.password);

    // Debug: Take screenshot after login to see what page we're on
    console.log('Current URL after login:', page.url());
    await page.screenshot({ path: 'after-login.png' });

    // Step 2: Create patient from RX page
    console.log('Step 2: Creating patient from RX page...');
    const patientName = TestDataLoader.generatePatientName(rxData.patientNamePrefix);
    const patientPhone = TestDataLoader.generatePatientPhone(rxData.phonePrefix);
    
    await prescriptionPage.createPatientFromRX(patientName, rxData.age, patientPhone);

    // Step 3: Add chief complaint
    console.log('Step 3: Adding chief complaint...');
    await prescriptionPage.addChiefComplaint(rxData.chiefComplaint);

    // Step 4: Save prescription
    console.log('Step 4: Saving prescription...');
    await prescriptionPage.savePrescription();

    console.log('TC-RX-01 completed successfully!');
  });
});
