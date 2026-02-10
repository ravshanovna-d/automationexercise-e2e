import pytest
import allure
from pages.home_page import HomePage
from pages.registration_page import RegistrationPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@allure.feature("E2E Purchase Flow")
@allure.story("Complete user journey from registration to order completion")
@pytest.mark.e2e
class TestE2EPurchase:
    
    @allure.title("Complete purchase flow: Registration → Add Products → Checkout")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_full_purchase_journey(self, page, base_url):
        """
        Test complete user journey:
        1. Register new user
        2. Add 2 products to cart
        3. Verify cart contents
        4. Complete checkout and payment
        """
        
        # Initialize page objects
        home = HomePage(page)
        registration = RegistrationPage(page)
        products = ProductsPage(page)
        cart = CartPage(page)
        checkout = CheckoutPage(page)
        
        # Generate unique user data
        test_name = "Test User"
        test_email = registration.generate_random_email()
        
        with allure.step("STEP 1: User Registration"):
            home.navigate(base_url)
            home.go_to_signup_login()
            registration.signup(test_name, test_email)
            registration.complete_registration()
            registration.verify_account_created()
            registration.click_continue()
        
        with allure.step("STEP 2: Add Products to Cart"):
            # Navigate directly to products page
            page.goto(f"{base_url}/products")
            # Wait for products container to be visible
            page.wait_for_selector("div.features_items", timeout=15000)
            # Small delay for page to settle
            page.wait_for_timeout(1000)
            
            products.add_first_product()
            products.add_second_product()
        
        with allure.step("STEP 3: Verify Cart"):
            cart.verify_product_count(expected_count=2)
            cart.proceed_to_checkout()
        
        with allure.step("STEP 4: Complete Purchase"):
            checkout.place_order()
            checkout.fill_payment_details()
            checkout.confirm_order()