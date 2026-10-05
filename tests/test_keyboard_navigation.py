import pytest
from pages.keyboard_navigation import Tabs

class TestTab:
    """A test suite to validate keyboard-only navigation workflows, tab-order sequencing, 
    and element focus shifting for user authentication flows.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Tabs keyboard navigation page object 
        and opens the login target view before running the test case.
        """
        self.tabs = Tabs(driver)
        self.tabs.open()

    def test_tab(self):
        """Simulates an authentication flow utilizing explicit tab keystrokes to input 
        credentials, submits the form, and asserts successful secure area entry.
        """
        flash_message = self.tabs.logging_in()
        assert "You logged into a secure area!" in flash_message
