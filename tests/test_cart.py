from pages.cart_working import Cart
import pytest
from utils.data_reader import DataReader
import os
from utils.logger import get_logger

logger = get_logger(__name__)

# Load external Excel-driven data inputs for testing shopping cart quantities
PYTEST_DATA = DataReader.read_file(os.path.abspath("test_data/cart_data.xlsx"))

PYTEST_DATA1 = [
    pytest.param(3, id="first"),
    pytest.param(2, id="second"),
    pytest.param(4, id="third")
]

class TestCart:
    """A test suite to validate end-to-end shopping cart functionality, including 

    adding items, verifying global cart item counts, and removing selections from the cart.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Cart page object, navigates 
        to the store page, and logs the user in before executing each test case.
        """
        self.cart_page = Cart(driver)
        self.cart_page.open()
        self.cart_page.login()

    @pytest.mark.parametrize("adding_num,cart_items_num", PYTEST_DATA)
    def test_item_in_cart(self, adding_num, cart_items_num):
        """Validates that adding a specific quantity of items dynamically updates 
        and reflects the correct total count when viewing the cart details page.
        """
        logger.info(f"Testing the {adding_num} items")
        self.cart_page.add_to_cart(adding_num)
        self.cart_page.go_to_cart()
        cart_items = self.cart_page.check_num_item_in_cart()
        logger.info(f"The cart items added are {cart_items}")
        assert cart_items_num == cart_items

    @pytest.mark.parametrize("item_num", PYTEST_DATA1)
    def test_removing_item(self, item_num):
        """Verifies that executing a removal interaction on a cart item successfully 
        updates its action button text and clears it from the active selection view.
        """
        removed_items = self.cart_page.check_remove_item_in_cart(item_num)
        assert "Remove" not in removed_items
