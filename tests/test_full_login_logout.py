from pages.full_login_logout import Login
import pytest

PYTEST_DATA = [
    pytest.param("tomsmith", "SuperSecretPassword!", "You logged into a secure area!", id="valid"),
    pytest.param("wrong", "wrong", "Your username is invalid!", id="invalid"),
    pytest.param("", "", "Your username is invalid!", id="empty")
]

class TestLogin:
    """A test suite to validate user authentication workflows, session state transitions, 
    and secure area logouts using data-driven test coverage.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Login page object and 
        navigates to the authentication page before each test case runs.
        """
        self.login_check = Login(driver)
        self.login_check.open()

    @pytest.mark.parametrize("name,password,flash", PYTEST_DATA)
    def test_loging_in(self, name, password, flash):
        """Validates login form submissions for valid, invalid, and empty credentials, 
        asserting flash message banner feedback accuracy and verifying full session 
        termination if access to the secure area is achieved.
        """
        flash_login = self.login_check.login(name, password)
        assert flash in flash_login
        if "logged into" in flash_login:
            flash_logout = self.login_check.logout()
            assert "You logged out of the secure area!" in flash_logout
