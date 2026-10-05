from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wb
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

class Drag_Dropdown:
    """A page object class to handle drag-and-drop interactions 
    on the Herokuapp Drag and Drop challenge page.
    """
    URL = "https://the-internet.herokuapp.com/drag_and_drop"
    A_COLUMN = (By.ID, "column-a")
    B_COLUMN = (By.ID, "column-b")

    def __init__(self, driver):
        """Initializes the Drag_Dropdown page object with a WebDriver instance and a 10-second explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = wb(self.driver, 10)

    def open(self):
        """Navigates the browser directly to the Herokuapp Drag and Drop challenge URL."""
        self.driver.get(self.URL)

    def draging_and_droping(self):
        """Simulates dragging Column A onto Column B using ActionChains 
        and retrieves the resulting text content of both columns.

        Returns:
            tuple: A pair of strings containing:
                - index 0 (str): The final text label displayed inside Column A post-interaction.
                - index 1 (str): The final text label displayed inside Column B post-interaction.
        """
        source = self.wait.until(ec.visibility_of_element_located(self.A_COLUMN))
        target = self.wait.until(ec.visibility_of_element_located(self.B_COLUMN))
        ActionChains(self.driver).drag_and_drop(source, target).perform()
        source_text = source.text
        target_text = target.text
        return (source_text, target_text)
