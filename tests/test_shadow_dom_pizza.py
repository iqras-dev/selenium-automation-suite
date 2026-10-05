import pytest
from pages.shadow_dom_pizza import RL  

PIZZA_DATA = [
    pytest.param("Pepperoni", "Pepperoni", id="Plain_text"),
    pytest.param("Margherita", "Margherita", id="Plain_text-1"),
    pytest.param("123", "123", id="numbers"),
    pytest.param("", "", id="empty")
]

class Testpizza:
    """A test suite to validate elements and text entry fields nested inside 
    Shadow DOM hosts on the pizza ordering page.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the RL shadow DOM page object and 
        navigates to its target URL before running each test case.
        """
        self.pizza_page = RL(driver)  
        self.pizza_page.open()

    def test_shadow_host(self):
        """Verifies basic access to the Shadow DOM by inserting a 'Pepperoni' value 
        and asserting that the found string returns as a boolean match.
        """
        value = self.pizza_page.pizza_find("Pepperoni")
        is_enter = value == "Pepperoni"
        assert is_enter

    @pytest.mark.parametrize("input_val,expected_output", PIZZA_DATA)
    def test_pizza_host(self, input_val, expected_output):
        """Validates that text values pass cleanly into the Shadow DOM input element 
        and match their expected outputs using data-driven inputs (text, numbers, and blanks).
        """
        output = self.pizza_page.pizza_find(input_val)
        assert output == expected_output
