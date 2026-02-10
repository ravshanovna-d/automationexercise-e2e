from playwright.sync_api import Page
import allure
import random
import string


class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Signup form
        self.signup_name_input = "input[data-qa='signup-name']"
        self.signup_email_input = "input[data-qa='signup-email']"
        self.signup_button = "button[data-qa='signup-button']"
        
        # Registration form
        self.gender_male = "#id_gender1"
        self.password_input = "#password"
        self.first_name_input = "#first_name"
        self.last_name_input = "#last_name"
        self.address_input = "#address1"
        self.country_dropdown = "#country"
        self.state_input = "#state"
        self.city_input = "#city"
        self.zipcode_input = "#zipcode"
        self.mobile_input = "#mobile_number"
        self.create_account_button = "button[data-qa='create-account']"
        
        # Success
        self.account_created_message = "h2[data-qa='account-created']"
        self.continue_button = "a[data-qa='continue-button']"
    
    @staticmethod
    def generate_random_email():
        """Generate unique email"""
        random_string = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        return f"testuser_{random_string}@example.com"
    
    @allure.step("Fill signup form with name: {name} and email: {email}")
    def signup(self, name: str, email: str):
        self.page.fill(self.signup_name_input, name)
        self.page.fill(self.signup_email_input, email)
        self.page.click(self.signup_button)
    
    @allure.step("Complete registration form")
    def complete_registration(self, password: str = "Test@1234"):
        self.page.check(self.gender_male)
        self.page.fill(self.password_input, password)
        
        self.page.fill(self.first_name_input, "Test")
        self.page.fill(self.last_name_input, "User")
        self.page.fill(self.address_input, "123 Test Street")
        
        self.page.select_option(self.country_dropdown, "United States")
        self.page.fill(self.state_input, "California")
        self.page.fill(self.city_input, "Los Angeles")
        self.page.fill(self.zipcode_input, "90001")
        self.page.fill(self.mobile_input, "1234567890")
        
        self.page.click(self.create_account_button)
    
    @allure.step("Verify account created successfully")
    def verify_account_created(self):
        assert self.page.is_visible(self.account_created_message)
        assert "ACCOUNT CREATED!" in self.page.inner_text(self.account_created_message)
    
    @allure.step("Click continue after registration")
    def click_continue(self):
        self.page.click(self.continue_button)
        # Wait for home page to load
        self.page.wait_for_timeout(2000)
        # Close any ads/popups
        try:
            self.page.click("button[aria-label='Close']", timeout=3000)
        except:
            pass

