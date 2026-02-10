from playwright.sync_api import Page
import allure


class ProductsPage:
    def __init__(self, page: Page):
        self.page = page
        
        # Locators
        self.first_product_add_to_cart = "(//div[@class='productinfo text-center']//a[@class='btn btn-default add-to-cart'])[1]"
        self.second_product_add_to_cart = "(//div[@class='productinfo text-center']//a[@class='btn btn-default add-to-cart'])[2]"
        self.continue_shopping_button = "button.btn-success"
        self.view_cart_link = "a[href='/view_cart'] u"
    
    @allure.step("Add first product to cart")
    def add_first_product(self):
        self.page.click(self.first_product_add_to_cart)
        self.page.wait_for_selector(self.continue_shopping_button, timeout=5000)
        self.page.click(self.continue_shopping_button)
    
    @allure.step("Add second product to cart")
    def add_second_product(self):
        self.page.click(self.second_product_add_to_cart)
        self.page.wait_for_selector(self.view_cart_link, timeout=5000)
        self.page.click(self.view_cart_link)

