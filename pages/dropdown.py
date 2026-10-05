from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as ec

class Selectdropdown:
    """A page object class to handle interactions with the Herokuapp Dropdown List page."""
    
    URL = "https://the-internet.herokuapp.com/dropdown"
    dd = (By.ID, "dropdown")

    def __init__(self, driver):
        """Initializes the Selectdropdown page object with a WebDriver instance and an explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open(self):
        """Navigates the browser directly to the Herokuapp Dropdown page URL."""
        self.driver.get(self.URL)

    def selection(self):
        """Selects options in the dropdown using both visible text and value attributes sequentially.

        Returns:
            tuple: A tuple containing two strings:
                - first (str): The visible text of the option selected by text ("Option 1").
                - second (str): The visible text of the option selected by value ("Option 1").
        """
        select_dropdown = self.wait.until(ec.visibility_of_element_located(self.dd))
        select = Select(select_dropdown)
        
        select.select_by_visible_text("Option 1") 
        first = select.first_selected_option.text
        
        select.select_by_value("1")
        second = select.first_selected_option.text
        return first, second

    def text_returning(self):
        """Selects a dropdown option by its visible text and retrieves its current selection text.

        Returns:
            str: The visible text of the selected option ("Option 1").
        """
        text_dropdown = self.wait.until(ec.visibility_of_element_located(self.dd))
        select = Select(text_dropdown)
        
        select.select_by_visible_text("Option 1")
        first = select.first_selected_option.text
        return first

    def value_returning(self):
        """Selects a dropdown option by its value attribute and retrieves its current selection text.

        Returns:
            str: The visible text of the selected option matching value "1" ("Option 1").
        """
        value_dropdown = self.wait.until(ec.visibility_of_element_located(self.dd))
        select = Select(value_dropdown)
        
        select.select_by_value("1")
        second = select.first_selected_option.text
        return second
