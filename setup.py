"""
    Undetected Geckodriver
    ======================
    This package provides a sophisticated wrapper around the
    webdriver.Firefox class from the Selenium package. It
    attempts to avoid detection by web services by patching
    certain parts of the Firefox browser.

    Author: Bytexenon (https://github.com/Bytexenon)
"""

# Imports #
import os
import re
from setuptools import setup

# Constants #
DIRNAME     = os.path.dirname(__file__)
DESCRIPTION = (
    "A Firefox Selenium WebDriver that patches the browser to avoid detection. "
    "Bypasses services such as Cloudflare, Distil Networks, and more. "
    "Ideal for web scraping, automated testing, and bot development without getting detected."
)
LONG_DESC   = open(os.path.join(DIRNAME, "README.md")).read()

# Read the version from the __init__.py file #
def find_version():
    with open(os.path.join(DIRNAME, 'undetected_geckodriver', '__init__.py'), encoding="utf-8") as f:
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", f.read(), re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")

# Setup #
setup(
    name='undetected-geckodriver',
    version=find_version(),
    packages=['undetected_geckodriver'],
    install_requires=[
        "selenium>=4.10.0"
    ],
    include_package_data=True,
    description=DESCRIPTION,
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    author='ByteXenon',
    author_email='ddavi142@asu.edu',
    url='https://github.com/ByteXenon/undetected_geckodriver',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    project_urls={
        'Documentation': 'https://github.com/ByteXenon/undetected_geckodriver#readme',
        'Source': 'https://github.com/ByteXenon/undetected_geckodriver',
        'Tracker': 'https://github.com/ByteXenon/undetected_geckodriver/issues',
        'Changelog': 'https://github.com/ByteXenon/undetected_geckodriver/releases',
    },
    keywords=(
        'selenium firefox webdriver undetected bypass cloudflare distil '
        'web scraping automated testing bot development anti-detection '
        'automation browser automation'
    ),
    python_requires='>=3.6',
    license='MIT',
)