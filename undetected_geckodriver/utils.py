# Imports #
import os
import sys
from selenium import webdriver

from .constants import REPLACEMENT_STRING, TO_REPLACE_STRING, SELENIUM_CONFIG_PATHS


# Functions #
def get_webdriver_instance() -> webdriver.Firefox:
    return webdriver.Firefox.__new__(webdriver.Firefox)


def get_firefox_installation_path() -> str:
    firefox_path = "/usr/lib/firefox"
    if not os.path.exists(firefox_path):
        raise FileNotFoundError("Could not find the Firefox path")
    return firefox_path


def get_selenium_configuration_path() -> str:
    os_type = sys.platform
    if os_type not in SELENIUM_CONFIG_PATHS:
        raise FileNotFoundError(f"Unsupported platform: {os_type}")

    for directory in SELENIUM_CONFIG_PATHS[os_type]:
        directory = directory.replace("$USER", os.getlogin())
        if os.path.exists(directory):
            return directory

    raise FileNotFoundError("Could not find the Selenium config path")


def create_undetected_firefox_directory(firefox_path: str, selenium_config_path: str) -> str:
    undetected_path = os.path.join(selenium_config_path, "undetected_firefox")
    #if os.path.exists(undetected_path):
    #    os.system(f"rm -rf {undetected_path}")

    if not os.path.exists(undetected_path):
        os.makedirs(undetected_path, exist_ok=True)
        os.system(f"cp -r {firefox_path}/* {undetected_path}")
    return undetected_path


def patch_libxul_file(undetected_path: str) -> None:
    libxul_path = os.path.join(undetected_path, "libxul.so")
    if not os.path.exists(libxul_path):
        raise FileNotFoundError("Could not find libxul.so (What the hell?!)")

    if len(REPLACEMENT_STRING) != len(TO_REPLACE_STRING):
        raise ValueError(
            "The length of REPLACEMENT_STRING must be equal to the length of TO_REPLACE_STRING"
        )

    libxul_data = None
    with open(libxul_path, "rb") as file:
        libxul_data = file.read()
    libxul_data = libxul_data.replace(TO_REPLACE_STRING, REPLACEMENT_STRING)
    with open(libxul_path, "wb") as file:
        file.write(libxul_data)
