"""
    Undetected Geckodriver
    ======================
    This package provides a sophisticated wrapper around the
    webdriver.Firefox class from the Selenium package. It
    attempts to avoid detection by web services by patching
    certain parts of the Firefox browser.

    Author: Bytexenon (https://github.com/Bytexenon)
"""

# Version #
__version__ = "1.0.4"

# Imports #
from .driver import Firefox
