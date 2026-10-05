from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as wb, Select
from selenium.webdriver.common.keys import Keys
from utils.logger import get_logger
class Cart:
        """
    Page object for Saucedemo cart functionality.
    Handles adding items to cart, navigating to cart,
    removing items and verifying cart contents.
    """

    URL="https://www.saucedemo.com"
    USERNAME=(By.ID,"user-name")
    PASSWORD=(By.ID,"password")
    LOGINBUTTON=(By.ID,"login-button")
    ITEM="//*[@id='inventory_container']/div/div"
    ADD_TO_CART= (By.CLASS_NAME, "btn_inventory")
    CART=(By.CSS_SELECTOR,".shopping_cart_link")
    REMOVE_BUTTON = (By.CSS_SELECTOR, ".btn.btn_secondary.btn_small.cart_button")
    CART_ITEMS="//*[@id='inventory_container']/div/div"
    REMOVED_ITEM=(By.CLASS_NAME,"removed_cart_item")
    CART_CONTAINER=(By.ID,"cart_contents_container")



    def __init__(self,driver):
        self.driver=driver
        self.wait=wb(self.driver,10)
        self.logger=get_logger(__name__)
    def open(self):
        self.driver.get(self.URL)
    def login(self):
        self.wait.until(ec.presence_of_element_located(self.USERNAME)).send_keys("standard_user")
        self.wait.until(ec.presence_of_element_located(self.PASSWORD)).send_keys("secret_sauce")
        self.wait.until(ec.presence_of_element_located(self.LOGINBUTTON)).click()
    def add_to_cart(self,num_items):
        """Adds specified number of items to cart from inventory page."""
        self.logger.info(f"Adding to cart {num_items} number of items")
        for i in range(num_items):
            item=self.wait.until(ec.presence_of_element_located((By.XPATH,self.ITEM+f"[{i+1}]")))
            item.find_element(*self.ADD_TO_CART).click()
    
    def go_to_cart(self):
        """Clicks cart icon to navigate to cart page."""
        self.wait.until(ec.presence_of_element_located(self.CART)).click()
    
    def del_cart_items(self,num_items):
        """Removes specified number of items from cart."""
        for i in range(num_items):
            btn = self.wait.until(ec.presence_of_element_located(self.REMOVE_BUTTON))
            btn.click()
            
    def check_num_item_in_cart(self):
        cart_items=self.wait.until(ec.presence_of_all_elements_located(self.CART_CONTAINER))
        return cart_items[0].text.count("Remove")

       
       
    def check_remove_item_in_cart(self,num_items):
        """Adds items, goes to cart, removes them all and returns remaining cart text."""
        self.add_to_cart(num_items)
        self.go_to_cart()
        self.del_cart_items(num_items)
        cart_items=self.wait.until(ec.presence_of_all_elements_located(self.CART_CONTAINER))
        return cart_items[0].text
       


        
