import pytest
from pages.dynamic_loading import DynamicLoadingPage
from selenium.common.exceptions import TimeoutException

PYTEST_DATA = [
    pytest.param(2, "Hello World!", False, id="too_fast_fail"),
    pytest.param(10, "Hello World!", True, id="patient_time")
]

class TestDynamicLoading:
    """A test suite to validate explicit wait strategies and boundary conditions 
    for elements that load dynamically via asynchronous requests on the web page.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the DynamicLoadingPage object and 
        navigates to the challenge page before each test execution.
        """
        self.page = DynamicLoadingPage(driver)
        self.page.open()

    @pytest.mark.parametrize("wait_time, expected_output, should_pass", PYTEST_DATA)    
    def test_loading_behavior(self, wait_time, expected_output, should_pass):
        """Validates dynamic element retrieval behavior by testing timeout limits, 
        ensuring a short wait correctly raises a TimeoutException and a sufficient 
        wait yields the expected content matching the assertion outcome.
        """
        self.page.click_start()
        
        if not should_pass:
            with pytest.raises(TimeoutException):
                self.page.get_finish_text(timeout=wait_time)
        else:
            output = self.page.get_finish_text(timeout=wait_time)
            assert output == expected_output
