from playwright.sync_api import Page
import allure


class HomePage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.signup_login_link = "a[href='/login']"
        self.products_link = "a[href='/products']"
        # Additional locators for navigation after login
        self.products_nav = "//a[@href='/products' and contains(text(), 'Products')]"
    
    @allure.step("Navigate to home page")
    def navigate(self, base_url: str):
        self.page.goto(base_url)
        # Wait for main content instead of networkidle
        self.page.wait_for_selector("div.features_items", timeout=10000)
    
    @allure.step("Click Signup/Login")
    def go_to_signup_login(self):
        self.page.click(self.signup_login_link)
    
    @allure.step("Navigate to products page")
    def go_to_products(self):
        # Close any popups/ads first
        try:
            # Try to close Google ad if present
            self.page.click("button[aria-label='Close']", timeout=3000)
        except:
            pass
        
        # Wait a bit for page to settle
        self.page.wait_for_timeout(2000)
        
        # Try different locators
        try:
            self.page.click(self.products_link, timeout=5000)
        except:
            # Fallback: use XPath locator
            self.page.click(self.products_nav, timeout=5000)