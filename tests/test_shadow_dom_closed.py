import pytest
from pages.shadow_dom_closed import Concept

PYTEST_DATA = [
    pytest.param("123", "123", id="nums"),
    pytest.param("abc", "abc", id="letters")
]

class TestConcept:
    """A test suite designed to validate interaction strategies and data extraction 
    on elements encapsulated inside a complex, closed Shadow DOM structure.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that instantiates the Concept page object class 
        and launches the target application page prior to every test execution.
        """
        self.concept_test = Concept(driver)
        self.concept_test.open()

    @pytest.mark.parametrize("input,output", PYTEST_DATA)
    def test_concept(self, input, output):
        """Validates that test data can be successfully passed into and read back from 
        a closed shadow root element, asserting the accuracy of the returned string value.
        """
        result = self.concept_test.shadow_dom_2(input)
        assert output == result
        print("The element block is closed")
