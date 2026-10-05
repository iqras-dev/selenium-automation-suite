from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
class Locate:
    """
    Page object for SelectorHub practice page.
    Demonstrates nested relative locators — finding password field
    between email and company inputs.
    """
    URL="https://selectorshub.com/xpath-practice-page/"
    EMAIL=(By.NAME,"email")
    COMPANY=(By.NAME,"company")
    PASSWORD=(By.ID,"pass")
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def open(self):
        self.driver.get(self.URL)
    def locate_password(self,password_enter):
        """Finds password input using above/below relative locators."""
        email=self.wait.until(lambda d: d.find_element(*self.EMAIL))
        company=self.wait.until(lambda d: d.find_element(*self.COMPANY))
        password=self.wait.until(lambda d: d.find_element(locate_with(By.TAG_NAME,"input").above(company).below(email)))
        password.send_keys(Keys.CONTROL+"a")
        password.send_keys(Keys.BACK_SPACE)
        password.send_keys(password_enter)
        return password.get_attribute("value")

