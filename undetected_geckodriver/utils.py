# Imports #
import os
import platform
import random
import shutil
import string
import sys

from selenium import webdriver

from .constants import PLATFORM_DEPENDENT_PARAMS, TO_REPLACE_STRING


# Functions #
def get_webdriver_instance() -> webdriver.Firefox:
    return webdriver.Firefox.__new__(webdriver.Firefox)


def get_firefox_installation_path() -> str:
    firefox_path = get_platform_dependent_params()["firefox_path"]
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
    xul = get_platform_dependent_params()["xul"]
    libxul_path = os.path.join(undetected_path, xul)
    if not os.path.exists(libxul_path):
        raise FileNotFoundError(f"Could not find the {xul} file")

    replacement_string = generate_random_string(len(TO_REPLACE_STRING))
    libxul_data = None
    with open(libxul_path, "rb") as file:
        libxul_data = file.read()
    libxul_data = libxul_data.replace(TO_REPLACE_STRING, replacement_string)
    with open(libxul_path, "wb") as file:
        file.write(libxul_data)


def get_platform_dependent_params() -> dict:
    system = platform.system()
    if system not in PLATFORM_DEPENDENT_PARAMS:
        raise OSError(f"Unsupported system: {system}")

    return PLATFORM_DEPENDENT_PARAMS[system]


def generate_random_string(length: int) -> str:
    return "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(length)
    )
