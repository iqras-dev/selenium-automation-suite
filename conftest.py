import pytest
import os
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure

# Appends the root directory path to sys.path to enable smooth internal cross-module imports
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

def pytest_addoption(parser):
    """Registers custom command-line arguments into the pytest engine interface configuration.

    Allows test runs to target specific browsers via CLI arguments (e.g., `pytest --browser=firefox`).
    """
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Browser to run test on: Chrome, Edge, Safari, Firefox"
    )

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """A pytest hook tracking lifecycle reports across execution phases (setup, call, teardown).
    
    Dynamically appends outcome states directly onto the active test node object to facilitate 
    downstream screenshot triggers on failures. Do not alter this structure.
    """
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(scope="class")
def driver(request):
    """Class-scoped browser setup and teardown fixture initializing specific WebDriver configurations 
    based on the command-line terminal selection option.

    Yields:
        WebDriver: An interactive, clean browser driver session instance.
    """
    browser = request.config.getoption("--browser").lower()
    
    if browser == "chrome":
        from selenium.webdriver.chrome.options import Options
        from selenium.webdriver.chrome.service import Service
        from webdriver_manager.chrome import ChromeDriverManager
        
        options = Options()
        options.add_argument("--start-maximized")
        options.add_argument("--incognito")
        
        # NATIVE REFACTOR FIX: Completely disables Chrome password manager popups natively 
        # so your Login test script flows smoothly without requiring pyautogui hacks or sleep delays.
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False
        })
        
        driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=options
        )

    elif browser == "firefox":
        from selenium.webdriver.firefox.options import Options
        from selenium.webdriver.firefox.service import Service
        from webdriver_manager.firefox import GeckoDriverManager
        
        options = Options()
        driver = webdriver.Firefox(
            service=Service(GeckoDriverManager().install()),
            options=options
        )

    elif browser == "safari":
        driver = webdriver.Safari()

    else:
        raise ValueError(f"Browser not supported: {browser}")
        
    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def screenshot_on_failure(driver, request):
    """An autouse method fixture monitoring execution lifecycle states post-call.
    
    If an internal failure state is registered via the test report hook metadata, it automatically 
    captures a webview snapshot and mirrors it into local storage files and interactive Allure reports.
    """
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        os.makedirs("screenshots", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        test_name = request.node.name
        filename = f"screenshots/{test_name}_{timestamp}.png"
        
        driver.save_screenshot(filename)
        print(f"\nScreenshot saved: {filename}")
        
        allure.attach(
            driver.get_screenshot_as_png(),
            name="screenshot",
            attachment_type=allure.attachment_type.PNG
        )
