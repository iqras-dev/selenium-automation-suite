import pytest
from pages.alerts_page import Alert


PYTEST_DATA = [
    pytest.param("Hi", "You entered: Hi", id="hi string"),
    pytest.param("123", "You entered: 123", id="num string")
]

class Testalert:
    """A test suite to validate modular individual interactions with basic JavaScript 
    Alerts, Confirmation boxes, and dynamic entry user Prompts.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that instantiates the localized alert page engine 
        and hits the practice site target page before every test run.
        """
        self.alerts = Alert(driver)
        self.alerts.open()

    def test_alert(self):
        """Triggers a standard JavaScript alert, handles its acknowledgement popup interface, 
        and asserts that the page accurately captures the successful click notification string.
        """
        output = self.alerts.click_alert()
        assert output == "You successfully clicked an alert"

    def test_confirm(self):
        """Triggers a standard verification confirm alert modal window, accepts the confirmation, 
        and verifies the matching resolution outcome banner text string state.
        """
        output = self.alerts.confirm_alert()
        assert output == "You clicked: Ok"

    @pytest.mark.parametrize("input,output", PYTEST_DATA)
    def test_prompt(self, input, output):
        """Validates dynamic string inputs passing cleanly through simulated browser text prompt inputs, 
        confirming that variable character strings match expected page output validations.
        """
        returned_value = self.alerts.prompt_alert(input)
        assert returned_value == output

