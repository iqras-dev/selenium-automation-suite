from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wb
from selenium.webdriver.support import expected_conditions as ec

class Windowhandle:
    """A page object class to handle complex multi-tab and multi-window navigation flows 
    on the Herokuapp Windows interaction page.
    """

    URL = "https://the-internet.herokuapp.com/windows"
    LINK = (By.LINK_TEXT, "Click Here")
    
    def __init__(self, driver):
        """Initializes the Windowhandle page object with a WebDriver instance and a 10-second explicit wait.

        Args:
            driver: The Selenium WebDriver instance used to interact with the browser.
        """
        self.driver = driver
        self.wait = wb(self.driver, 10.0)

    def open(self):
        """Navigates the browser directly to the Herokuapp Multi-Window challenge URL."""
        self.driver.get(self.URL)

    def window_title(self):
        """Triggers a secondary browser tab creation, switches execution focus to it to extract 
        its header title string, closes the tab, and returns safely back to the parent window context.

        Returns:
            str: The raw window title of the newly spawned browser tab (e.g., "New Window").
        """
        main_window = self.driver.current_window_handle
        current = self.driver.window_handles
        self.wait.until(ec.element_to_be_clickable(self.LINK)).click()
        self.wait.until(ec.new_window_is_opened(current))   
        
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break
                
        title = self.driver.title
        self.driver.close()
        self.driver.switch_to.window(main_window)
        return title 

    def get_dict(self):
        """Spawns a new tab, captures both its page title and absolute address URL properties 
        as an isolated structured dictionary, terminates the child view, and regains parent focus.

        Returns:
            dict: A key-value collection mapping containing:
                - "title" (str): The child page title string.
                - "url" (str): The child page target absolute link endpoint string.
        """
        main_window = self.driver.current_window_handle
        current = self.driver.window_handles
        self.wait.until(ec.element_to_be_clickable(self.LINK)).click()
        self.wait.until(ec.new_window_is_opened(current))
        
        all_windows = self.driver.window_handles
        for window in all_windows:
            if window != main_window:
                self.driver.switch_to.window(window)
                break
                
        # Declared locally inside the method to prevent cross-test dictionary state cross-contamination
        result_dict = {}
        result_dict["title"] = self.driver.title
        result_dict["url"] = self.driver.current_url
        
        self.driver.close()
        self.driver.switch_to.window(main_window)
        return result_dict

    def get_tuple(self):
        """Spawns a new tab, switches context to extract properties from both the child target 
        and historical parent context, completely cleans up the generated child view, and maps them to a tuple.

        Returns:
            tuple: A pair collection sequence containing:
                - index 0 (str): The title text string from the newly generated sub-view window.
                - index 1 (str): The title text string from the initial parent landing window context.
        """
        main_window = self.driver.current_window_handle
        current = self.driver.window_handles
        self.wait.until(ec.element_to_be_clickable(self.LINK)).click()
        self.wait.until(ec.new_window_is_opened(current))
        
        all_windows = self.driver.window_handles
        new_window = None
        for window in all_windows:
            if window != main_window:
                new_window = window
                self.driver.switch_to.window(new_window)
                break
                
        title_new_window = self.driver.title
    
        self.driver.switch_to.window(main_window)
        title_main_window = self.driver.title
        result = (title_new_window, title_main_window)
  
        if new_window:
            self.driver.switch_to.window(new_window)
            self.driver.close()
            self.driver.switch_to.window(main_window)

        return result
