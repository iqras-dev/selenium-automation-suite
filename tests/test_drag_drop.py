import pytest
from pages.drag_and_drop import Drag_Dropdown

class TestDragDropdown:
    """A test suite to validate drag-and-drop structural box element manipulation 
    and subsequent cell label content changes.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Drag_Dropdown page object 
        and opens the challenge page before each test case runs.
        """
        self.drag_drop = Drag_Dropdown(driver)
        self.drag_drop.open()

    def test_drag_drop(self):
        """Executes the drag-and-drop workflow, unpacks the resulting text labels, 
        and asserts that Column A and Column B successfully swapped their text titles.
        """
        result = self.drag_drop.draging_and_droping()
        A, B = result
        assert A == "B"
        assert B == "A"
