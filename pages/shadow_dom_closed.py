from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
class Concept:
        """
    Page object for SelectorHub nested Shadow DOM practice.
    Demonstrates accessing elements inside closed shadow DOM
    using nested shadow root traversal.
    """

    URL="https://selectorshub.com/xpath-practice-page/"
    HOST1=(By.CSS_SELECTOR,"#userName")
    HOST2=(By.CSS_SELECTOR,"#concepts")
    CONCEPT=(By.CSS_SELECTOR,"#training")
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(self.driver,10)
    def open(self):
        self.driver.get(self.URL)
    def shadow_dom_2(self,text):
        """
        Attempts to access element inside closed shadow DOM.
        Navigates through nested shadow roots to reach target element.
        """
        host1=self.wait.until(ec.presence_of_element_located(self.HOST1))
        shadow_root1=host1.shadow_root
        host2=shadow_root1.find_element(*self.HOST2)
        shadow_root2=host2.shadow_root
        concept=shadow_root2.find_element(*self.CONCEPT)
        concept.send_keys(Keys.CONTROL+"a")
        concept.send_keys(Keys.BACK_SPACE) 
        concept.send_keys(text)
        concept.send_keys(Keys.ENTER)
        concept_text=concept.get_attribute("value")
        return concept_text   
     
