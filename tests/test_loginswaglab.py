from pages.login_page_swaglab import SwagLab
import pytest
from utils.data_reader import DataReader
import os
from utils.logger import get_logger
import allure

# Parse Excel columns dynamically into clean, named pytest parameters
PYTEST_DATA = DataReader.excel_to_pytest_param(os.path.abspath("test_data/login_data.xlsx"))
logger = get_logger(__name__)

@allure.epic("Saucedemo App")
@allure.feature("Authentication")
class TestLogin:
    """A comprehensive test suite covering standard, edge-case, and invalid user login workflows, 
    session token creation, application redirection, and final session closure.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that instantiates the SwagLab authentication Page Object 
        and hits the storefront landing page ahead of every scenario.
        """
        self.login_page = SwagLab(driver)
        self.login_page.open()

    @pytest.mark.parametrize("username,password,expected", PYTEST_DATA)
    @allure.title("Valid user can login and logout")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_login(self, username, password, expected):
        """Executes a multi-tier credentials matrix using external data sources; asserts page object routing flags 
        for positive flows (followed by clean logouts) and checks validation message accuracy on failures.
        """
        logger.info(f"Running with username {username}")
        login_successful = self.login_page.login(username, password)
        logger.info(f"The successful login occured  as {login_successful}")
        
        if login_successful:
            condition = self.login_page.logout()
            assert condition == True
        else:
            error_message = self.login_page.get_error_message()
            assert expected in error_message
