from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wb
from selenium.webdriver.support import expected_conditions as ec
import os

class Files:
    """A page object class to handle interactions with the Herokuapp File Uploader page."""
    
    URL = "http://the-internet.herokuapp.com/upload"
    FILE_INPUT = (By.NAME, "file")
    FILE_SUBMIT = (By.ID, "file-submit")
    FILE_UPLOAD = (By.ID, "uploaded-files")

    def __init__(self, driver):
        """Initializes the Files page object with a WebDriver instance and an explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = wb(self.driver, 10.0)

    def open(self):
        """Navigates the browser directly to the Herokuapp File Uploader page URL."""
        self.driver.get(self.URL)

    def uploading_file(self, file_name):
        """Uploads a specified file by sending its path to the file input element, 
        submitting the form, and confirming the successful upload.

        Args:
            file_name (str): The absolute or relative system path of the file to be uploaded.

        Returns:
            str: The text confirmation showing the name of the successfully uploaded file.
        """
        file_input = self.wait.until(ec.presence_of_element_located(self.FILE_INPUT))
        file_input.send_keys(file_name)
        self.wait.until(ec.element_to_be_clickable(self.FILE_SUBMIT)).click()
        result = self.wait.until(ec.presence_of_element_located(self.FILE_UPLOAD)).text
        return result
