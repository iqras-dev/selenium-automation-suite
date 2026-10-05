from pages.inventory_page import Inventroy
import pytest
from utils.data_reader import DataReader
import os

# Load external data driven inputs for testing dropdown sort logic
PYTEST_DATA = DataReader.read_file(os.path.abspath("test_data/inventory_sort_data.csv"))

PYTEST_DATA1 = [
    pytest.param(1, 2, 3, id="first"),
    pytest.param(2, 3, 4, id="second"),
    pytest.param(3, 4, 5, id="third"),
    pytest.param(4, 5, 6, id="fourth")
]

PYTEST_DATA2 = [
    pytest.param(1, 2, id="first"),
    pytest.param(3, 4, id="second"),
    pytest.param(4, 5, id="third"),
    pytest.param(5, 6, id="fourth")
]

class TestInventory:
    """A test suite validating product catalog sorting, structural title validation, 

    and multi-item shopping cart integration workflows on Swag Labs.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the inventory page, navigates 
        to the storefront URL, and completes the login sequence before each test case execution.
        """
        self.inventory_page = Inventroy(driver)
        self.inventory_page.open()
        self.inventory_page.login_in()

    @pytest.mark.parametrize("sort_value,sort_option,expected", PYTEST_DATA)    
    def test_sort_low_to_high(self, sort_value, sort_option, expected):
        """Validates that selecting a catalog sorting strategy returns the correct 
        first item price based on external CSV data inputs.
        """
        price = self.inventory_page.sort_prices(sort_value, sort_option)
        assert price == expected

    def test_page_tilte(self):
        """Verifies that the sub-header label matches the expected store header text 'Products'."""
        resutl = self.inventory_page.check_page_title()
        assert resutl == "Products"
    
    @pytest.mark.parametrize("index1,index2,index3", PYTEST_DATA1)
    def test_price(self, index1, index2, index3):
        """Validates that sorting products from low-to-high pricing progressively 
        increases item costs across three indexed elements.
        """
        prices = self.inventory_page.finding_price_for_first_item(index1, index2, index3)
        first_item = float(prices[0])
        second_item = float(prices[1])
        third_item = float(prices[2])
        assert second_item >= first_item
        assert third_item >= second_item

    @pytest.mark.parametrize("index1,index2", PYTEST_DATA2)
    def test_cart_count(self, index1, index2):
        """Asserts that adding inventory items to the cart progressively increments 
        the global application cart badge totals.
        """
        counts = self.inventory_page.counting_cart_items(index1, index2)
        print(counts)
        count1 = int(counts[0])
        count2 = int(counts[1])
        assert count2 > count1
