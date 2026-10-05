from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wb
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as ec

class Tabs:
    """A page object class to handle keyboard-based navigation and authentication 

    on the Herokuapp Login page.
    """
    URL = "https://the-internet.herokuapp.com/login"
    FLASH = (By.ID, "flash")
    USERNAME = (By.ID, "username")

    def __init__(self, driver):
        """Initializes the Tabs page object with a WebDriver instance and a 10-second explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = wb(self.driver, 10)

    def open(self):
        """Navigates the browser directly to the Herokuapp Login page URL."""
        self.driver.get(self.URL)

    def logging_in(self):
        """Authenticates by focusing on the username field and executing a sequence of 

        tab-based keyboard strokes to input credentials, submit the form, and return 
        the status message text.

        Returns:
            str: The raw text confirmation message displayed in the resulting flash banner.
        """
        user_name = self.wait.until(ec.presence_of_element_located(self.USERNAME))
        user_name.send_keys("tomsmith")
        user_name.send_keys(Keys.TAB)
        
        active_element = self.driver.switch_to.active_element
        active_element.send_keys(Keys.TAB)
        active_element.send_keys("SuperSecretPassword!")
        active_element.send_keys(Keys.ENTER)
        
        flash_message = self.wait.until(ec.presence_of_element_located(self.FLASH))
        return flash_message.text
