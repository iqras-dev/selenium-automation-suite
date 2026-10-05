from selenium.webdriver.common.by import By
from selenium.webdriver.support import  expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait,Select
from selenium.webdriver.common.keys import Keys
class Frame:
        """
    Page object for nested frames practice on the-internet.herokuapp.com.
    Demonstrates switching between nested frames using parent_frame()
    and default_content().
    """
    URL="https://the-internet.herokuapp.com/nested_frames"
    TOP=(By.NAME,"frame-top")
    LEFT=(By.NAME,"frame-left")
    RIGHT=(By.NAME,"frame-right")
    MIDDLE=(By.NAME,"frame-middle")
    BOTTOM=(By.NAME,"frame-bottom")
    BODY=(By.TAG_NAME,"body")
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
    def open(self):
        self.driver.get(self.URL)
    def frame_dict_creation(self):
        """
        Navigates through all nested frames and collects text.
        Returns:
            dict: Frame texts with keys 'left', 'right', 'middle', 'bottom'
        """
        frame_dict={}
        #top frame
        self.wait.until(ec.frame_to_be_available_and_switch_to_it(self.TOP))
        #left frame
        self.wait.until(ec.frame_to_be_available_and_switch_to_it(self.LEFT))
        left_body=self.wait.until(ec.presence_of_element_located(self.BODY))
        frame_dict["left"]=left_body.text
        self.driver.switch_to.parent_frame()
        #right frame
        self.wait.until(ec.frame_to_be_available_and_switch_to_it(self.RIGHT))
        right_body=self.wait.until(ec.presence_of_element_located(self.BODY))
        frame_dict["right"]=right_body.text
        self.driver.switch_to.parent_frame()
        #middle frame
        self.wait.until(ec.frame_to_be_available_and_switch_to_it(self.MIDDLE))
        middle_body=self.wait.until(ec.presence_of_element_located(self.BODY))
        frame_dict["middle"]=middle_body.text
        self.driver.switch_to.default_content()
        #bottom frame
        self.wait.until(ec.frame_to_be_available_and_switch_to_it(self.BOTTOM))
        bottom_body=self.wait.until(ec.presence_of_element_located(self.BODY))
        frame_dict["bottom"]=bottom_body.text
        self.driver.switch_to.default_content()
        return frame_dict


