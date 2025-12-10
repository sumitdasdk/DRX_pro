import { Page, Locator } from '@playwright/test';
import { BasePage } from './BasePage';

/**
 * LoginPage contains all selectors and methods related to login functionality
 */
export class LoginPage extends BasePage {
  // Selectors
  private usernameField: Locator;
  private passwordField: Locator;
  private loginButton: Locator;

  constructor(page: Page) {
    super(page);
    this.usernameField = page.getByRole('textbox', { name: 'Username' });
    this.passwordField = page.getByRole('textbox', { name: 'Password' });
    this.loginButton = page.getByRole('button', { name: 'Login' });
  }

  /**
   * Navigate to login page
   */
  async navigateToLogin() {
    await this.goto('http://digital-rx-pro.s3-website-us-east-1.amazonaws.com/');
    await this.wait(1000);
  }

  /**
   * Perform login with credentials
   */
  async login(username: string, password: string) {
    await this.fillField(this.usernameField, username);
    await this.fillField(this.passwordField, password);
    
    // Wait for navigation while clicking login
    await Promise.all([
      this.waitForURL('**/doctor/rx', 30000),
      this.clickElement(this.loginButton)
    ]);
    
    // Wait for RX page to fully load
    await this.wait(3000);
  }

  /**
   * Login with default credentials (Sadman/Sadman1#)
   */
  async loginAsDoctor() {
    await this.login('Sadman', 'Sadman1#');
  }

  /**
   * Get doctor name from top right corner
   */
  async getDoctorName(): Promise<string> {
    const doctorNameElement = this.page.getByRole('button', { name: 'User' }).first().locator('p');
    await this.waitForElement(doctorNameElement, 10000);
    return await doctorNameElement.textContent() || '';
  }

  /**
   * Check if logged in by verifying URL contains doctor/rx
   */
  isLoggedIn(): boolean {
    return this.getURL().includes('doctor/rx');
  }
}
