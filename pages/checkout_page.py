from playwright.sync_api import Page
import allure


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.place_order_button = "a[href='/payment']"
        self.name_on_card_input = "input[data-qa='name-on-card']"
        self.card_number_input = "input[data-qa='card-number']"
        self.cvc_input = "input[data-qa='cvc']"
        self.expiry_month_input = "input[data-qa='expiry-month']"
        self.expiry_year_input = "input[data-qa='expiry-year']"
        self.confirm_order_button = "button[data-qa='pay-button']"
        self.success_message = "p"
    
    @allure.step("Click Place Order")
    def place_order(self):
        self.page.click(self.place_order_button)
    
    @allure.step("Fill payment details")
    def fill_payment_details(self):
        self.page.fill(self.name_on_card_input, "Test User")
        self.page.fill(self.card_number_input, "4532015112830366")
        self.page.fill(self.cvc_input, "123")
        self.page.fill(self.expiry_month_input, "12")
        self.page.fill(self.expiry_year_input, "2027")
    
    @allure.step("Confirm order and verify success")
    def confirm_order(self):
        self.page.click(self.confirm_order_button)
        
        # Wait for success
        self.page.wait_for_selector(self.success_message, timeout=10000)
        success_text = self.page.inner_text(self.success_message)
        assert "Congratulations! Your order has been confirmed!" in success_text