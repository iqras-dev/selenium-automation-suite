from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Dynamicloading:
    """A page object class to handle interactions with the Herokuapp Dynamic Loading (Example 1) page."""
    
    START = (By.CSS_SELECTOR, "#start button")
    FINSH_TXT = (By.CSS_SELECTOR, "#finish h4")

    def __init__(self, driver):
        """Initializes the Dynamicloading page object with a WebDriver instance.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        
    def open(self):
        """Navigates the browser directly to the Herokuapp Dynamic Loading Example 1 page URL."""
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def loading(self, time_pass):
        """Triggers the dynamic loading process by clicking the start button, 
        waits for the hidden element to become visible, and captures its text.

        Args:
            time_pass (int or float): The maximum number of seconds to wait for elements 
                to become visible before throwing a TimeoutException.

        Returns:
            str: The text content of the dynamically loaded finish element (e.g., "Hello World!").
        """
        self.wait = WebDriverWait(self.driver, time_pass)
        self.wait.until(EC.visibility_of_element_located(self.START)).click()
        return self.wait.until(EC.visibility_of_element_located(self.FINSH_TXT)).text
