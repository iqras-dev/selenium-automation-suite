import pytest
from pages.files import Files
import os

class TestFiles:
    """A test suite to validate local file generation and successful multi-part 
    form upload operations on the application web page.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Files page object and 
        navigates to the file uploader challenge view prior to running each test case.
        """
        self.setup_file = Files(driver)
        self.setup_file.open()

    def test_creat_files(self):
        """Dynamically generates a temporary local text file asset, passes its absolute path 
        to the upload form control, and asserts that the application UI accurately returns 
        the matching file name upon completion.
        """
        file_new = os.path.abspath("sample_file.txt")
        with open(file_new, "w") as f:
            f.write("File context")
            
        result = self.setup_file.uploading_file(file_new)
        assert result == "sample_file.txt"
