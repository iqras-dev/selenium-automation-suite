import pytest
from pages.hover import Hover

PYTEST_DATA = [
    pytest.param(0, "name: user1", id="first"),
    pytest.param(1, "name: user2", id="second"),
    pytest.param(2, "name: user3", id="third")
]

class TestHover:
    """A test suite to validate mouse cursor hover events and the subsequent 
    rendering of hidden user overlay captions on the web view.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Hover page object and 
        navigates to the hovers interaction path before executing each test case.
        """
        self.hovering = Hover(driver)
        self.hovering.open()

    @pytest.mark.parametrize("index,figure_caption", PYTEST_DATA)
    def test_hover(self, index, figure_caption):
        """Validates that hovering the mouse cursor over a target profile element at a specific index 
        dynamically exposes and matches the correct underlying user descriptive caption text.
        """
        text = self.hovering.hovering_over_images(index)
        assert text == figure_caption
