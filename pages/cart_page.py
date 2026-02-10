from playwright.sync_api import Page
import allure


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.cart_items = "tr[id^='product-']"
        self.proceed_to_checkout_button = "a.btn-default.check_out"
    
    @allure.step("Verify cart contains {expected_count} products")
    def verify_product_count(self, expected_count: int = 2):
        actual_count = self.page.locator(self.cart_items).count()
        assert actual_count == expected_count, f"Expected {expected_count} products, found {actual_count}"
    
    @allure.step("Proceed to checkout")
    def proceed_to_checkout(self):
        self.page.click(self.proceed_to_checkout_button)