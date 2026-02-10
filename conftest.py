import pytest
from playwright.sync_api import sync_playwright, Browser, Page
import allure


@pytest.fixture(scope="session")
def browser():
    """Launch Google Chrome browser"""
    with sync_playwright() as p:
        browser = p.chromium.launch(
            channel="chrome",  # Use installed Google Chrome
            headless=False,    # Show browser window
            slow_mo=500        # Slow down for visibility
        )
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser: Browser):
    """Create new page for each test"""
    context = browser.new_context(
        viewport={"width": 1920, "height": 1080}
    )
    page = context.new_page()
    
    yield page
    
    # Screenshot on failure
    try:
        allure.attach(
            page.screenshot(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    except:
        pass  # Ignore screenshot errors
    
    try:
        page.close()
        context.close()
    except:
        pass

@pytest.fixture(scope="function", autouse=True)
def base_url():
    """Base URL for the application"""
    return "https://www.automationexercise.com"