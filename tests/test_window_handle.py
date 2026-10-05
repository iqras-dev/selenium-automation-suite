import pytest
from pages.window_handle1 import Windowhandle

class TestWindowHandle:
    """Tests for multiple window handling — title, url, and tuple retrieval."""

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Windowhandle page object and 
        opens the initial multi-window challenge page view prior to running each test case.
        """
        self.window_handle = Windowhandle(driver)
        self.window_handle.open()

    def test_window_handle(self):
        """Validates basic browser tab context switching by invoking a secondary window trigger, 
        and asserting that the newly focused window title matches 'New Window'.
        """
        title = self.window_handle.window_title()
        assert title == "New Window"

    def test_dict(self):
        """Verifies structured dictionary-based window metrics extraction by validating that both 
        the target sub-window title and its specific absolute URL properties match requirements.
        """
        result = self.window_handle.get_dict()
        assert result["title"] == "New Window"
        assert result["url"] == "https://the-internet.herokuapp.com/windows/new"

    def test_tuple(self):
        """Validates complex tab state storage and historical retrieval tracking by unpacking 
        a returned collection tuple and asserting the structural names of both the newly opened 
        sub-window and the initial parent web view.
        """
        result = self.window_handle.get_tuple()
        first, second = result

        assert first == "New Window"
        assert second == "The Internet"
