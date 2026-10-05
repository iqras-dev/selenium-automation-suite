import pytest
from pages.relative_locator_country import RL

PYTEST_DATA = [
    pytest.param("124", "124", id="simple_nums"),
    pytest.param("3546", "3546", id="sm2")
]

class Testlocator:
    """A test suite to validate relative element location, text manipulation, and input capturing 
    specifically for country-based data forms or grids using Selenium Relative Locators.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the RL country locator page object and 
        navigates to its designated page before each test execution.
        """
        self.start = RL(driver)
        self.start.open()

    @pytest.mark.parametrize("input,expected_output", PYTEST_DATA)
    def test_rl(self, input, expected_output):
        """Validates that numerical values pass cleanly into elements targeted by 
        relative position parameters and asserts the correctness of the returned string.
        """
        value = self.start.locate(input)
        assert value == expected_output
