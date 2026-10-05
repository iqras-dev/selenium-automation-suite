import pytest
from pages.dynamic_loading import Dynamicloading
from selenium.common.exceptions import TimeoutException
import time

PYTEST_DATA = [
    pytest.param(2, "Hello World!", False, id="to_fast_fail"),
    pytest.param(10, "Hello World!", True, id="Patient_time")
]

class Testdynamic:
    """A test suite to validate explicit wait strategies and boundary conditions 
    for elements that load dynamically via asynchronous requests on the web page.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Dynamicloading page object and 
        navigates to the challenge page before each test execution.
        """
        self.page = Dynamicloading(driver)
        self.page.open()

    @pytest.mark.parametrize("wait_time,expected_output,should_pass", PYTEST_DATA)    
    def test_loading(self, wait_time, expected_output, should_pass):
        """Validates dynamic element retrieval behavior by testing timeout limits, 
        ensuring a short wait correctly raises a TimeoutException and a sufficient 
        wait yields the expected content matching the assertion outcome.
        """
        if not should_pass:
            with pytest.raises(TimeoutException):
                self.page.loading(wait_time)
        else:
            output = self.page.loading(wait_time)
            pass_test = output == expected_output
            assert pass_test == should_pass
