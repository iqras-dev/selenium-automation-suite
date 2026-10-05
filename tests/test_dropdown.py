import pytest
from pages.dropdown import Selectdropdown

PYTEST_DATA = [
    pytest.param("Option 1", id="1"),
    pytest.param("Option 1", id="2")
]

class TestDropdown:
    """A test suite to validate dropdown field component rendering, visible text selections, 
    and matching database value attribute configurations.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Selectdropdown page object and 
        navigates to the dropdown utility view before running each test case.
        """
        self.select = Selectdropdown(driver)
        self.select.open()

    def test_selection_first(self):
        """Verifies combined text and value attribute parsing logic by checking that both 
        approaches resolve to the correct chosen element string.
        """
        first, second = self.select.selection()
        assert first == "Option 1"
        assert second == "Option 1"

    @pytest.mark.parametrize("option", PYTEST_DATA)    
    def test_selection_second(self, option):
        """Validates decoupled independent dropdown lookup methods via parameterization, 
        confirming individual visible text and internal values return identical visual names.
        """
        first = self.select.text_returning()
        second = self.select.value_returning()
        assert first == option
        assert second == option
