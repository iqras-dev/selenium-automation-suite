from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wb
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class Context_click:
    """A page object class to handle interactions with the Herokuapp Context Menu page."""
    
    URL = "https://the-internet.herokuapp.com/context_menu"
    BOX = (By.ID, "hot-spot")

    def __init__(self, driver):
        """Initializes the Context_click page object with a WebDriver instance and a standard explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = wb(self.driver, 10)

    def open(self):
        """Navigates the browser directly to the Herokuapp Context Menu page URL."""
        self.driver.get(self.URL)

    def context_clicking(self):
        """Performs a right-click (context click) on the target box element, 
        waits for the resulting JavaScript alert to appear, and dismisses it.

        Returns:
            str: The text content contained inside the JavaScript alert.
        """
        box_element = self.wait.until(ec.visibility_of_element_located(self.BOX))
        ActionChains(self.driver).context_click(box_element).perform()
        
        alert = self.wait.until(ec.alert_is_present())
        text = alert.text
        alert.accept()
        return text
