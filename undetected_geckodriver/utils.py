# Imports #
import os
import sys
import shutil

from selenium import webdriver
from .constants import REPLACEMENT_STRING, TO_REPLACE_STRING, UNDETECTED_FIREFOX_PATHS


# Functions #
def get_webdriver_instance() -> webdriver.Firefox:
    return webdriver.Firefox.__new__(webdriver.Firefox)


def get_firefox_installation_path() -> str:
    firefox_path = _get_platform_dependent_params()["firefox_path"]
    if not os.path.exists(firefox_path):
        raise FileNotFoundError("Could not find the Firefox path")
    return firefox_path


def get_undetected_firefox_path() -> str:
    system = sys.platform
    login = os.getlogin()
    if system not in UNDETECTED_FIREFOX_PATHS:
        raise OSError(f"Unsupported system: {system}")

    path = UNDETECTED_FIREFOX_PATHS[system].replace("$USER", login)
    return path


def create_undetected_firefox_directory(firefox_path: str, undetected_path: str) -> str:
    if not os.path.exists(undetected_path):
        shutil.copytree(firefox_path, undetected_path)
    return undetected_path


def patch_libxul_file(undetected_path: str) -> None:
    xul = _get_platform_dependent_params()["xul"]
    libxul_path = os.path.join(undetected_path, xul)
    if not os.path.exists(libxul_path):
        raise FileNotFoundError(f"Could not find {xul} (What the hell?!)")

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


def _get_platform_dependent_params() -> dict:
    match sys.platform:
        case "win32":
            return {"firefox_exec": "firefox.exe", "firefox_path": "C:\\Program Files\\Mozilla Firefox", "xul": "xul.dll"}
        case "darwin":
            return {"firefox_exec": "Firefox.app", "firefox_path": "/Applications/Firefox.app/Contents/MacOS", "xul": "libxul.dylib"}
        case _:
            return {"firefox_exec": "firefox", "firefox_path": "/usr/lib/firefox", "xul": "libxul.so"}