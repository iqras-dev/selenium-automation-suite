import pytest
from pages.iframe_tinymce import Frames

PYTEST_DATA = [
    pytest.param("abc", "abc", id="letter"),
    pytest.param("123", "123", id="nums"),
    pytest.param("@#$", "@#$", id="sybmols")
]

class Testframe:
    """A test suite to validate switching driver execution contexts into single inline frames (iframes) 
    and verifying text entry behaviors inside embedded rich text editors.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Frames iframe page object and 
        navigates to its target URL before running each test case.
        """
        self.frame = Frames(driver)
        self.frame.open()

    @pytest.mark.parametrize("input,output", PYTEST_DATA)
    def test_iframe(self, input, output):
        """Validates that text values pass cleanly into the embedded iframe's input field 
        and match their expected outputs using data-driven strings (letters, numbers, and symbols).
        """
        result = self.frame.type_text(input)
        assert result == output
