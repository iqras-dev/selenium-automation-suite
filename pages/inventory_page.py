
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait as wb, Select
from selenium.webdriver.common.keys import Keys

class Inventroy:
    """A page object class to handle e-commerce flows on the Swag Labs (SauceDemo) storefront, 
    including authentication, sorting products, and cart operations.
    """
    URL = "https://www.saucedemo.com/"
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGINBUTTON = (By.ID, "login-button")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".title")
    CARTCOUNT = (By.CSS_SELECTOR, "#shopping_cart_container > a")
    SORT_CONTAINER = (By.CSS_SELECTOR, ".product_sort_container")
    INVENTORYLIST = (By.XPATH, "//*[@id='inventory_container']/div")
    PRICE = (By.CSS_SELECTOR, ".inventory_item_price")
    INVENTORYCONTAINER = (By.ID, "inventory_container")
    FIRST_ITEM = (By.XPATH, "//*[@id='inventory_container']/div/div[1]")
    SECOND_ITEM = (By.XPATH, "//*[@id='inventory_container']/div/div[2]")
    THIRD_ITEM = (By.XPATH, "//*[@id='inventory_container']/div/div[3]")
    ADD_TO_CART = (By.CLASS_NAME, "btn_inventory")
    ITEM = "//*[@id='inventory_container']/div/div"

    def __init__(self, driver):
        """Initializes the Inventroy page object with a WebDriver instance and a 10-second explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = wb(self.driver, 10)

    def open(self):
        """Navigates the browser directly to the Swag Labs login page URL."""
        self.driver.get(self.URL)

    def login_in(self):
        """Logs into the application using preset standard user credentials."""
        self.wait.until(ec.presence_of_element_located(self.USERNAME)).send_keys("standard_user")
        self.wait.until(ec.presence_of_element_located(self.PASSWORD)).send_keys("secret_sauce")
        self.wait.until(ec.element_to_be_clickable(self.LOGINBUTTON)).click()

    def check_page_title(self):
        """Retrieves the header text of the inventory page to verify a successful login redirect.

        Returns:
            str: The page sub-header text (e.g., "Products").
        """
        product_title = self.wait.until(ec.presence_of_element_located(self.PRODUCT_TITLE)) 
        return product_title.text
    
    def cart_count(self):
        """Retrieves the numeric badge value displayed on the shopping cart icon.

        Returns:
            str: The string representation of the total items inside the shopping cart.
        """
        num_item_in_cart = self.wait.until(ec.presence_of_element_located(self.CARTCOUNT))
        return num_item_in_cart.text
    
    def sort_low_to_high(self):
        """Applies the product catalog sorting option to filter items by price from low to high."""
        dropdown = self.wait.until(ec.presence_of_element_located(self.SORT_CONTAINER))
        select = Select(dropdown)
        select.select_by_value("lohi")

    def sort_prices(self, sort_value, sort_option):
        """Selects a specified sorting strategy and returns the price of the first element if 

        the applied sorting description matches the validation option string.

        Args:
            sort_value (str): The value attribute of the sorting option (e.g., "lohi", "hilo").
            sort_option (str): The expected text label of the selected sorting option to validate against.

        Returns:
            str or None: The currency text of the first inventory item if validation passes; otherwise None.
        """
        dropdown = self.wait.until(ec.presence_of_element_located(self.SORT_CONTAINER))
        select = Select(dropdown)
        select.select_by_value(sort_value)
        
        dropdown = self.wait.until(ec.presence_of_element_located(self.SORT_CONTAINER))
        select = Select(dropdown)
        result = select.first_selected_option.text
        
        first_element = self.wait.until(ec.visibility_of_element_located(self.FIRST_ITEM))
        price_of_first_element = first_element.find_element(*self.PRICE)
        if result == sort_option:
            return price_of_first_element.text

    def finding_price_for_first_item(self, index1, index2, index3):
        """Sorts the inventory from low to high and strips the leading currency sign ($) 

        from the prices of three items selected by their collection index numbers.

        Args:
            index1 (int or str): The XPath collection position index for the first targeted item.
            index2 (int or str): The XPath collection position index for the second targeted item.
            index3 (int or str): The XPath collection position index for the third targeted item.

        Returns:
            tuple: A tuple containing three strings representing numerical prices without dollar signs 
                (e.g., ("7.99", "9.99", "15.99")).
        """
        self.sort_low_to_high()
        first_item = self.wait.until(ec.presence_of_element_located((By.XPATH, self.ITEM + f"[{index1}]")))
        first_item_price = first_item.find_element(*self.PRICE)
        
        second_item = self.wait.until(ec.presence_of_element_located((By.XPATH, self.ITEM + f"[{index2}]")))
        second_item_price = second_item.find_element(*self.PRICE)
        
        third_item = self.wait.until(ec.presence_of_element_located((By.XPATH, self.ITEM + f"[{index3}]")))
        third_item_price = third_item.find_element(*self.PRICE)
        return first_item_price.text[1:], second_item_price.text[1:], third_item_price.text[1:]
    
    def adding_to_cart_item(self, index1):
        """Locates an inventory item by its index position and clicks its corresponding 'Add to cart' button.

        Args:
            index1 (int or str): The XPath collection position index of the item to append to the cart.
        """
        first_item = self.wait.until(ec.presence_of_element_located((By.XPATH, self.ITEM + f"[{index1}]")))
        first_item.find_element(*self.ADD_TO_CART).click()
        print("First_item_added to cart")

    def counting_cart_items(self, index1, index2):
        """Adds two distinct items to the shopping cart sequentially and snapshots the cart badge total 

        after each inclusion.

        Args:
            index1 (int or str): The collection index of the first item to add.
            index2 (int or str): The collection index of the second item to add.

        Returns:
            tuple: A tuple containing two strings representing the progressive cart item quantities 
                (e.g., ("1", "2")).
        """
        self.adding_to_cart_item(index1)
        count1 = self.cart_count()
        self.adding_to_cart_item(index2)
        count2 = self.cart_count()
        return count1, count2
