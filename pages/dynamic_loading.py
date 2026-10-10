from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class DynamicLoadingPage:
    """A page object class to handle interactions with the Herokuapp Dynamic Loading (Example 1) page."""
    
    START_BUTTON = (By.CSS_SELECTOR, "#start button")
    FINISH_TEXT = (By.CSS_SELECTOR, "#finish h4")

    def __init__(self, driver, default_timeout=10):
        """Initializes the page object with a WebDriver instance and a default explicit wait.

        Args:
            driver: The Selenium WebDriver instance.
            default_timeout (int or float): Default max seconds to wait for elements.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, default_timeout)
        
    def open(self):
        """Navigates the browser directly to the Herokuapp Dynamic Loading Example 1 page URL."""
        self.driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

    def click_start(self):
        """Triggers the dynamic loading process by clicking the start button."""
        self.wait.until(EC.visibility_of_element_located(self.START_BUTTON)).click()

    def get_finish_text(self, timeout=None):
        """Waits for the hidden element to become visible and captures its text.

        Args:
            timeout (int or float, optional): Override the default timeout for this specific check.

        Returns:
            str: The text content of the dynamically loaded finish element.
        """
        waiter = WebDriverWait(self.driver, timeout) if timeout else self.wait
        return waiter.until(EC.visibility_of_element_located(self.FINISH_TEXT)).text
