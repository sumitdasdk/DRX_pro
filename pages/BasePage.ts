import { Page, Locator } from '@playwright/test';

/**
 * BasePage class contains common actions that can be used across all page objects
 * This promotes code reusability and reduces duplication
 */
export class BasePage {
  protected page: Page;

  constructor(page: Page) {
    this.page = page;
  }

  /**
   * Navigate to a URL
   */
  async goto(url: string) {
    await this.page.goto(url, { waitUntil: 'domcontentloaded', timeout: 90000 });
  }

  /**
   * Fill a text field with value
   */
  async fillField(locator: Locator, value: string) {
    await locator.waitFor({ state: 'visible', timeout: 10000 });
    await locator.fill(value);
  }

  /**
   * Click an element
   */
  async clickElement(locator: Locator) {
    await locator.waitFor({ state: 'visible', timeout: 15000 });
    await locator.click();
  }

  /**
   * Click by role
   */
  async clickByRole(role: string, name: string, exact: boolean = false) {
    const locator = exact
      ? this.page.getByRole(role as any, { name, exact })
      : this.page.getByRole(role as any, { name });
    await this.clickElement(locator);
  }

  /**
   * Get locator by role
   */
  getByRole(role: string, name: string, exact: boolean = false) {
    return exact
      ? this.page.getByRole(role as any, { name, exact })
      : this.page.getByRole(role as any, { name });
  }

  /**
   * Get locator by test ID
   */
  getByTestId(testId: string) {
    return this.page.getByTestId(testId);
  }

  /**
   * Get locator by text
   */
  getByText(text: string) {
    return this.page.getByText(text);
  }

  /**
   * Get locator by CSS selector
   */
  locator(selector: string) {
    return this.page.locator(selector);
  }

  /**
   * Wait for URL to match pattern
   */
  async waitForURL(urlPattern: string, timeout: number = 30000) {
    await this.page.waitForURL(urlPattern, { timeout });
  }

  /**
   * Wait for element to be visible
   */
  async waitForElement(locator: Locator, timeout: number = 10000) {
    await locator.waitFor({ state: 'visible', timeout });
  }

  /**
   * Simple timeout delay
   */
  async wait(milliseconds: number) {
    await this.page.waitForTimeout(milliseconds);
  }

  /**
   * Press a keyboard key
   */
  async pressKey(key: string) {
    await this.page.keyboard.press(key);
  }

  /**
   * Get page URL
   */
  getURL() {
    return this.page.url();
  }

  /**
   * Evaluate JavaScript in page context
   */
  async evaluate(script: string | (() => any), arg?: any) {
    return await this.page.evaluate(script as any, arg);
  }
}
