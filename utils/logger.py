import os 
from datetime import datetime
import logging

def get_logger(name):
    """Factory configuration function initializing structural execution log tracks by splitting 
    outputs between persistent file directories and clear, interactive terminal screens.

    Args:
        name (str): The naming space tracking context (typically passed as `__name__`) determining 
            the explicit module origin of log emissions.

    Returns:
        logging.Logger: A configured, active logging interface context ready for runtime status reporting.
    """
    # create logs folder
    os.makedirs("logs", exist_ok=True)
    
    # create logger
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    
    if not logger.handlers:
        timespan = datetime.now().strftime("%Y %m %d")
        
        # creating file handler
        file_handler = logging.FileHandler(f"logs/tests_{timespan}.log")
        file_handler.setLevel(logging.DEBUG)
        
        # console handler shown in terminal
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # formatter
        formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s", datefmt="%Y-%m-%d %H%M%S")
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger
