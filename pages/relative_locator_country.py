from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys

class RL:
    """
    Page object for SelectorHub practice page.
    Demonstrates relative locator usage with locate_with.
    """
    URL = "https://selectorshub.com/xpath-practice-page/"
    ML = (By.XPATH, "//label[contains(text(),'Mobile Number')]")
    CL = (By.XPATH, "//label[contains(text(),'Country')]")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.URL)

    def locate(self, number):
        """Finds country input using relative locator and enters number."""
        mobile_label = self.wait.until(lambda x: x.find_element(*self.ML))
        country_label = self.wait.until(lambda x: x.find_element(*self.CL))
        country_input = self.wait.until(
            lambda x: x.find_element(
                locate_with(By.TAG_NAME, "input").below(country_label)
            )
        )
        country_input.send_keys(Keys.CONTROL + "a")
        country_input.send_keys(Keys.BACK_SPACE)
        country_input.send_keys(number)
        return country_input.get_attribute("value")
