from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
class Frames:
     """
    Page object for iFrame practice on the-internet.herokuapp.com.
    Demonstrates switching into an iFrame and interacting with
    the TinyMCE rich text editor inside it.
    """
    URL= "https://the-internet.herokuapp.com/iframe"
    IFRAME_ELEMENT =(By.ID,"mce_0_ifr")
    EDIT_ELEMENT = (B y.TAG_NAME,"body")
    def __init__(self,driver):
        self.driver= driver
        self.wait= WebDriverWait(self.driver,10)

    def open(self):
        self.driver.get(self.URL)
    def type_text(self,text):
                """
        Switches into TinyMCE iFrame, types text and returns typed content.
        Note: May fail if TinyMCE is in read-only mode due to API limits.
        """

        iframe= self.driver.find_element(*self.IFRAME_ELEMENT )
        self.driver.switch_to.frame(iframe)
        editor= self.driver.find_element(*self.EDIT_ELEMENT )
        editor.clear()
        editor.send_keys(text)
        typed_text= editor.get_attribute("innerHTML")
        self.driver.switch_to.default_content()
        return typed_text
        
