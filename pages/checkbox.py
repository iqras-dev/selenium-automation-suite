from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class Checkboxes:
    """
    Page object for checkbox practice on the-internet.herokuapp.com.
    Demonstrates finding, selecting and verifying checkbox states.
    """
    URL = "https://the-internet.herokuapp.com/checkboxes"
    CB = (By.CSS_SELECTOR, "input[type='checkbox']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def get_checkboxes(self):
        """Returns list of all checkbox elements on the page."""
        return self.wait.until(EC.visibility_of_all_elements_located(self.CB))

    def select_all_checkboxes(self, checkboxes):
        """Checks all unchecked checkboxes."""
        for cb in checkboxes:
            if not cb.is_selected():
                cb.click()

    def toggle_checkbox(self, index, checkboxes):
        """Toggles checkbox at given index if not already selected."""
        if not checkboxes[index].is_selected():
            checkboxes[index].click()

    def get_status(self, checkboxes):
        """Returns list of boolean values representing checkbox states."""
        return [cb.is_selected() for cb in checkboxes]
