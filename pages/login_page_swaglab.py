from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as wb
from selenium.webdriver.common.keys import Keys
from utils.logger import get_logger

class SwagLab:
    """A page object class to handle direct user authentication and session states 
    on the Swag Labs application.
    """
    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGINBUTTON = (By.ID, "login-button")
    APPLOGO = (By.CSS_SELECTOR, ".app_logo")
    SIDE_BUTTON = (By.CSS_SELECTOR, "#react-burger-menu-btn")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".title")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    ERROR_MESSAGE = (By.CSS_SELECTOR, ".error-message-container.error")
    LOGIN_CONTAINER = (By.CSS_SELECTOR, ".login_container")

    def __init__(self, driver):
        """Initializes the SwagLab page object with a WebDriver instance, explicit wait, and logger.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = wb(self.driver, 10)
        self.logger = get_logger(__name__)

    def open(self):
        """Navigates the browser directly to the Swag Labs application landing page."""
        self.driver.get(self.URL)

    def login(self, username, password):
        """Fills out the credentials form, submits it, and verifies whether the user redirected 

        successfully to the product dashboard page.

        Args:
            username (str): The username credentials text.
            password (str): The password credentials text.

        Returns:
            bool: True if authentication succeeded and the product title became available; 
                False otherwise.
        """
        self.logger.info(f"Attempting login with username: {username}")
        self.wait.until(ec.presence_of_element_located(self.USERNAME)).send_keys(username)
        self.wait.until(ec.presence_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(ec.presence_of_element_located(self.LOGINBUTTON)).click()
        
        try:
            product = self.wait.until(ec.presence_of_element_located(self.PRODUCT_TITLE)) 
            return True
        except:
            self.logger.error(f"Login failed: {username}")  
            return False
        
    def logout(self):
        """Opens the navigation sidebar, clicks the logout hyperlink option, and verifies 

        redirection back to the storefront login panel.

        Returns:
            bool or None: True if the login panel layout container becomes interactive post-click.
        """
        self.wait.until(ec.presence_of_element_located(self.SIDE_BUTTON)).click()
        self.wait.until(ec.element_to_be_clickable(self.LOGOUT_BUTTON)).click()
        login_container = self.wait.until(ec.element_to_be_clickable(self.LOGIN_CONTAINER))
        if login_container:
            return True

    def get_error_message(self):
        """Captures and returns the text string embedded within the explicit form validation error element.

        Returns:
            str: The target validation error feedback message content.
        """
        error_message = self.wait.until(ec.presence_of_element_located(self.ERROR_MESSAGE))
        return error_message.text
