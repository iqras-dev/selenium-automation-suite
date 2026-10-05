from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wb
from selenium.webdriver.support import expected_conditions as ec

class Alert:
    """A page object class to handle triggering and interacting with unique JavaScript 
    Alerts, Confirms, and Prompts on the Herokuapp JavaScript Alerts page.
    """
    URL = "https://herokuapp.com"
    JS_ALERT = (By.XPATH, "//button[text()='Click for JS Alert']")
    JS_CONFIRM = (By.XPATH, "//button[text()='Click for JS Confirm']")
    JS_PROMPT = (By.XPATH, "//button[text()='Click for JS Prompt']")
    Result = (By.ID, "result")

    def __init__(self, driver):
        """Initializes the Alert page object with a WebDriver instance and a 10-second explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = wb(self.driver, 10)

    def open(self):
        """Navigates the browser directly to the Herokuapp JavaScript Alerts page URL."""
        self.driver.get(self.URL)

    def click_alert(self):
        """Clicks the simple JS Alert button, accepts the browser popup dialog, 
        and extracts the resulting page validation text.

        Returns:
            str: The confirmation status text string displayed on the page layout view.
        """
        self.wait.until(ec.element_to_be_clickable(self.JS_ALERT)).click()
        self.wait.until(ec.alert_is_present()).accept()
        return self.wait.until(ec.presence_of_element_located(self.Result)).text

    def confirm_alert(self):
        """Clicks the JS Confirm button, accepts the browser confirmation dialog box, 
        and extracts the resulting page validation text.

        Returns:
            str: The confirmation status text string displayed on the page layout view.
        """
        self.wait.until(ec.element_to_be_clickable(self.JS_CONFIRM)).click()
        self.wait.until(ec.alert_is_present()).accept()
        return self.wait.until(ec.presence_of_element_located(self.Result)).text

    def prompt_alert(self, text_to_send):
        """Clicks the JS Prompt button, injects a dynamic string input value into the field, 
        accepts the dialog, and extracts the resulting page validation text.

        Args:
            text_to_send (str): The dynamic text string parameter to submit inside the prompt popup input box.

        Returns:
            str: The confirmation status text string displayed on the page layout view.
        """
        self.wait.until(ec.element_to_be_clickable(self.JS_PROMPT)).click()
        alert = self.wait.until(ec.alert_is_present())
        alert.send_keys(text_to_send)
        alert.accept()
        return self.wait.until(ec.presence_of_element_located(self.Result)).text
