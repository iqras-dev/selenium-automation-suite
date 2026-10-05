from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wb
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class Login:
    """A page object class to handle authentication and session termination on the Herokuapp Login page."""
    
    URL = "https://herokuapp.com"
    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.CSS_SELECTOR, "button[type='submit']")
    FLASH = (By.ID, "flash")
    LOGOUT = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def __init__(self, driver):
        """Initializes the Login page object with a WebDriver instance and a standard explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = wb(self.driver, 10)

    def open(self):
        """Navigates the browser directly to the Herokuapp Login page URL."""
        self.driver.get(self.URL)

    def login(self, name, password):
        """Fills out the authentication credentials, submits the form, and returns 
        the resulting flash message banner text.

        Args:
            name (str): The account username string.
            password (str): The account password string.

        Returns:
            str: The raw text content extracted from the resulting flash message banner.
        """
        self.wait.until(ec.presence_of_element_located(self.USERNAME)).send_keys(name)
        self.wait.until(ec.presence_of_element_located(self.PASSWORD)).send_keys(password)
        self.wait.until(ec.element_to_be_clickable(self.LOGIN)).click()        
        flash = self.wait.until(ec.presence_of_element_located(self.FLASH))
        return flash.text

    def logout(self):
        """Clicks the logout button from the secure area and handles the redirect banner text.

        Returns:
            str: The raw text content extracted from the exit flash message banner.
        """
        self.wait.until(ec.element_to_be_clickable(self.LOGOUT)).click()
        flash = self.wait.until(ec.presence_of_element_located(self.FLASH))
        return flash.text
