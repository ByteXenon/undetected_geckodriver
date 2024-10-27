<div align="center">

# Undetected GeckoDriver v1.0.4

A Python package that acts as an interface between your code and Selenium, preventing detection by services like Cloudflare.

[![PyPI version](https://badge.fury.io/py/undetected-geckodriver.svg)](https://badge.fury.io/py/undetected-geckodriver)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/undetected-geckodriver)](https://pepy.tech/project/undetected-geckodriver)
[![Downloads](https://pepy.tech/badge/undetected-geckodriver/month)](https://pepy.tech/project/undetected-geckodriver)
[![Downloads](https://pepy.tech/badge/undetected-geckodriver/week)](https://pepy.tech/project/undetected-geckodriver)

</div>

## Overview

This project is a Python package that utilizes the [Selenium](https://github.com/SeleniumHQ/selenium) package, a powerful browser automation framework that lets you control your browser through code. When browsers are controlled by scripts (often referred to as "puppet browsers"), they typically set specific properties that can be detected by services like Cloudflare. For instance, properties such as `navigator.webdriver` can be checked using JavaScript scripts, which may restrict access to content on sites protected by such services.

To address this issue, Undetected Geckodriver acts as an interface between your code and Selenium. When you create a new WebDriver instance using the `Firefox()` class from the Undetected GeckoDriver package (as opposed to using Selenium directly), the following processes occur:

1. The original Firefox binary is located, copied, and patched to prevent it modifying properties such as `navigator.webdriver` while using Selenium.
2. A Selenium WebDriver instance is created that uses the patched Firefox binary.

## Installation

You can install the package via pip:

```bash
pip install undetected-geckodriver
```

Or you can install it from source.

```bash
git clone https://github.com/ByteXenon/undetected_geckodriver --depth 1
cd undetected_geckodriver
pip install .
```

Note, that the last example is not supported, and you shouldn't use it unless you want to modify the package.

## Usage

Since Undetected GeckoDriver acts as an interface for Selenium, you can use it the same way you would use Selenium.

You can integrate Undetected GeckoDriver into your existing Selenium code by simply replacing the `selenium.webdriver.Firefox` imports with `undetected_geckodriver.Firefox`.

Here are a couple of examples demonstrating how you can use this project:

1. **Creating a new undetected WebDriver instance and navigating to example.com**:

```python
from undetected_geckodriver import Firefox

driver = Firefox()
driver.get("https://www.example.com")
```

2. **Searching for "Undetected Geckodriver 1337!" on Google**:

```python
import time
from undetected_geckodriver import Firefox
from selenium.webdriver.common.by import By

# Constants
SEARCH_FOR = "Undetected Geckodriver 1337!"
GOOGLE_URL = "https://www.google.com"

# Initialize the undetected Firefox browser
driver = Firefox()

# Navigate to Google
driver.get(GOOGLE_URL)

# Locate the search box and perform the search
search_box = driver.find_element(By.NAME, "q")  # Find the search box in the DOM (Document Object Model)
search_box.send_keys(SEARCH_FOR)  # Input the search term
search_box.submit()  # Submit the search

# Wait for the page to load
time.sleep(2)

# Print the current URL after the search
print("Current URL:", driver.current_url)

# Wait for a while to observe the results
time.sleep(15)

# Ensure the browser is closed
driver.quit()  # Close the browser
```

For further information and advanced usage, you can take a look at the [official Selenium documentation](https://www.selenium.dev/documentation/en/) since Undetected GeckoDriver is built on top of Selenium.

## Requirements

- Python 3.6+
- Selenium 4.10.0+

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request if you encounter any problems or have any suggestions, improvements, or new features you would like to see implemented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the contributors of the Selenium project.
- Inspiration from the [undetected-chromedriver project](https://github.com/ultrafunkamsterdam/undetected-chromedriver).
