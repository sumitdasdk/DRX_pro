import * as fs from 'fs';
import * as path from 'path';

/**
 * Helper class to load and access test data from JSON file
 */
export class TestDataLoader {
  private static testData: any = null;

  /**
   * Load test data from Transfer_TestData.json
   */
  static loadTestData() {
    if (!this.testData) {
      const testDataPath = path.join(__dirname, '../test-data/Transfer_TestData.json');
      const fileContent = fs.readFileSync(testDataPath, 'utf-8');
      this.testData = JSON.parse(fileContent);
    }
    return this.testData;
  }

  /**
   * Get login credentials
   */
  static getLoginData() {
    return this.loadTestData().login;
  }

  /**
   * Get patient test data for a specific test case
   */
  static getPatientData(testCaseId: string) {
    return this.loadTestData().patient[testCaseId];
  }

  /**
   * Get prescription test data for a specific test case
   */
  static getPrescriptionData(testCaseId: string) {
    return this.loadTestData().prescription[testCaseId];
  }

  /**
   * Get URL patterns
   */
  static getUrls() {
    return this.loadTestData().urls;
  }

  /**
   * Get timeout values
   */
  static getTimeouts() {
    return this.loadTestData().timeouts;
  }

  /**
   * Get specific timeout value
   */
  static getTimeout(timeoutName: string): number {
    return this.loadTestData().timeouts[timeoutName] || 10000;
  }

  /**
   * Generate unique patient name with timestamp
   */
  static generatePatientName(prefix: string): string {
    return `${prefix}_${Date.now()}`;
  }

  /**
   * Generate unique patient phone with timestamp
   */
  static generatePatientPhone(phonePrefix: string): string {
    const timestamp = Date.now();
    return phonePrefix + String(timestamp).slice(-4);
  }
}
