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

from setuptools import setup
from undetected_geckodriver import __version__

# Constants #
DIRNAME     = os.path.dirname(__file__)
DESCRIPTION = (
  "A custom Firefox WebDriver that attempts to avoid detection by web services.",
  "Can bypass Cloudflare/hCaptcha/etc. detections."
)
LONG_DESC   = open(os.path.join(DIRNAME, "README.md")).read()

# Setup #
setup(
    name='undetected-geckodriver',
    version=__version__,
    packages=['undetected_geckodriver'],
    install_requires=[
        "selenium>=4.10.0"
    ],
    include_package_data=True,
    description='A custom Firefox WebDriver that attempts to avoid detection by web services.',
    author='ByteXenon',
    author_email='ddavi142@asu.edu',
    url='https://github.com/ByteXenon/undetected_geckodriver',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    project_urls={
        'Documentation': 'https://github.com/ByteXenon/undetected_geckodriver#readme',
        'Source': 'https://github.com/ByteXenon/undetected_geckodriver',
        'Tracker': 'https://github.com/ByteXenon/undetected_geckodriver/issues',
    },
    long_description=LONG_DESC,
    long_description_content_type='text/markdown',
    python_requires='>=3.6',
    License='MIT',
)