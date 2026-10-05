import pytest 
from pages.nested_frame import Frames

class TestFrames:
    """A test suite to validate data extraction across multiple nested frames 

    and sub-frames on the web page.
    """

    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Autouse setup fixture that initializes the Frames page object and 
        navigates to the frames page before executing each test case.
        """
        self.frames = Frames(driver)
        self.frames.open()

    def test_frames(self):
        """Extracts text content from multiple frames (left, right, middle, and bottom) 
        and verifies that each frame displays its correct expected label string.
        """
        dict_frame = self.frames.frames()
        assert dict_frame["left"].strip() == "LEFT"
        assert dict_frame["right"].strip() == "RIGHT"
        assert dict_frame["middle"].strip() == "MIDDLE"
        assert dict_frame["bottom"].strip() == "BOTTOM"
