import pytest
from pages.context_click import Context_click

class TestContext:
    """A test suite to validate right-click (context click) operations and subsequent 
    JavaScript alert handling on the application's context menu zone.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Context_click page object and 
        navigates to the challenge page before each test case runs.
        """
        self.choosing_box = Context_click(driver)
        self.choosing_box.open()

    def test_contexting(self):
        """Simulates a right-click inside the designated hot-spot box area, grabs 
        the text displayed on the resulting JavaScript pop-up alert, and asserts its message accuracy.
        """
        text = self.choosing_box.context_clicking()
        assert "You selected a context menu" in text
