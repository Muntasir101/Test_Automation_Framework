# URL of the application under test
URL = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"

# Browser options (you can customize these as needed)
BROWSER = "chrome"  # Options: "chrome", "firefox", etc.


# config.py
import logging

# Logging configuration
LOGGING_LEVEL = logging.INFO
LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOGGING_FILENAME = "./logs/test.log"




