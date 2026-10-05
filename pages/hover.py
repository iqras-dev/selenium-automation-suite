from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait as wb
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys

class Hover:
    """A page object class to handle mouse hover interactions and capture hidden profile data 
    on the Herokuapp Hovers page.
    """
    
    URL = "https://the-internet.herokuapp.com/hovers"
    FIGURES = (By.CLASS_NAME, "figure")
    FIGURE_TEXT = (By.TAG_NAME, "h5")

    def __init__(self, driver):
        """Initializes the Hover page object with a WebDriver instance and a standard explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = wb(self.driver, 10)

    def open(self):
        """Navigates the browser directly to the Herokuapp Hovers page URL."""
        self.driver.get(self.URL)

    def hovering_over_images(self, index_fig):
        """Simulates hovering the mouse cursor over a specific user profile card by its index 
        and extracts the hidden username header text that appears.

        Args:
            index_fig (int): The 0-based index of the target profile image card to hover over (e.g., 0, 1, or 2).

        Returns:
            str: The text content of the visible header element revealing the user name (e.g., "name: user1").
        """
        figures = self.wait.until(ec.visibility_of_all_elements_located(self.FIGURES))

        ActionChains(self.driver).move_to_element(figures[index_fig]).perform()
        TEXT = figures[index_fig].find_element(*self.FIGURE_TEXT).text
        return TEXT
