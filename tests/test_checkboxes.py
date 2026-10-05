import pytest
from pages.checkbox import Checkboxes

PyTEST_DATA = [
    pytest.param(0, True, id="first_checkbox"),
    pytest.param(1, True, id="second_checkbox")
]

class TestCheckboxe:
    """A test suite to validate the interaction and selection states of multiple 

    checkbox elements on the web page.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Checkboxes page object and 
        navigates to its target URL before running each test case.
        """
        self.login = Checkboxes(driver)
        self.login.open()

    def test_checkboxes(self):
        """Verifies bulk selection functionality by interacting with all retrieved checkboxes 
        and asserting that every single checkbox is successfully marked as checked.
        """
        checkboxes = self.login.get_checkboxe()
        self.login.select_checkboxes(checkboxes)
        status_list = self.login.get_status(checkboxes)
        all_checked = all(status_list) == True
        assert all_checked, f"Not every checkbox is checked"

    @pytest.mark.parametrize("input_value, output_expected", PyTEST_DATA)
    def test_params(self, input_value, output_expected):
        """Validates individual checkbox manipulation using data-driven inputs, ensuring that 
        toggling a specific checkbox index results in the expected boolean selection status.
        """
        checkboxes = self.login.get_checkboxe()
        self.login.checkbox_for_test(input_value, checkboxes)
        status = self.login.get_status(checkboxes)[input_value]
        assert status == output_expected
