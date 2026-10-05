from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class RL:
    """A page object class to handle automation scenarios involving complex web controls 
    and open Shadow DOM elements on the SelectorsHub practice page.
    """
    URL = "https://selectorshub.com/xpath-practice-page/"

    def __init__(self, driver):
        """Initializes the RL page object with a WebDriver instance and a 10-second explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        """Navigates the browser directly to the SelectorsHub XPath Practice page URL."""
        self.driver.get(self.URL)

    def pizza_find(self, input_text):
        """Uses JavaScript execution to breach the shadow boundary, locates the hidden pizza input box 
        nested inside the open shadow root, updates its text content, and verifies the resulting state.

        Args:
            input_text (str): The text content or value to be populated inside the target Shadow DOM input field.

        Returns:
            str: The current value attribute present inside the input element post-interaction to validate input accuracy.
        """
        pizza_box = self.driver.execute_script(
            "return document.querySelector('#app2').shadowRoot.querySelector('#pizza')"
        )
        pizza_box.send_keys(Keys.CONTROL + "a")
        pizza_box.send_keys(Keys.BACK_SPACE)
        pizza_box.send_keys(input_text)
        return pizza_box.get_attribute("value")
