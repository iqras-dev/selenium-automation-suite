import pytest
from pages.relative_locators import Locate

PYTEST_DATA = [
    pytest.param("wrong_pass", "wrong_pass", id="wrong_password"),
    pytest.param("SuperSecretPassword!", "SuperSecretPassword!", id="right_password")
]

class TestLocator:
    """A test suite to validate element identification and text entry using 
    Selenium Relative Locators (e.g., above, below, to_left_of, to_right_of).
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Locate page object and 
        navigates to the challenge page before each test execution.
        """
        self.start_page = Locate(driver)
        self.start_page.open()

    @pytest.mark.parametrize("input,expected_output", PYTEST_DATA)
    def test_locating(self, input, expected_output):
        """Validates that credentials can be filled into a relative target field 
        and verifies that the returned value matches the expected state.
        """
        output = self.start_page.locate_password(input)
        assert output == expected_output
