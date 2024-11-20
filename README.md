<div align="center">

# Undetected GeckoDriver v1.0.6

A Python package that integrates with Firefox Selenium to bypass anti-bot detection mechanisms, ideal for web scraping, automated testing, and browser automation without being marked as a bot.

[![PyPI version](https://badge.fury.io/py/undetected-geckodriver.svg)](https://badge.fury.io/py/undetected-geckodriver)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Downloads](https://pepy.tech/badge/undetected-geckodriver)](https://pepy.tech/project/undetected-geckodriver)
[![Downloads](https://pepy.tech/badge/undetected-geckodriver/month)](https://pepy.tech/project/undetected-geckodriver)
[![Downloads](https://pepy.tech/badge/undetected-geckodriver/week)](https://pepy.tech/project/undetected-geckodriver)

</div>

## Preview

|                                           With undetected-geckodriver                                           |                                           Without undetected-geckodriver                                           |
| :-------------------------------------------------------------------------------------------------------------: | :----------------------------------------------------------------------------------------------------------------: |
| ![With undetected-geckodriver](https://github.com/user-attachments/assets/24a208c0-4793-4d5d-bf3c-22e3a1beb9a4) | ![Without undetected-geckodriver](https://github.com/user-attachments/assets/927be4df-06d6-4d88-8948-668c35efa68e) |

> You can test it for yourself by going to [this website](https://www.browserscan.net/bot-detection)

## Overview

> [!NOTE]
> Currently, this package only supports Linux. Support for Windows and macOS is planned for future releases.

Undetected GeckoDriver is a powerful Python package designed to work seamlessly with the [Selenium](https://github.com/SeleniumHQ/selenium) browser automation framework. Selenium allows you to control web browsers through code, making it an essential tool for web scraping, automated testing, and browser automation. However, when browsers are controlled by scripts (often referred to as "puppet browsers"), they typically set specific properties that can be detected by anti-bot services like Cloudflare. For instance, properties such as `navigator.webdriver` can be checked using JavaScript, which may restrict access to content on sites protected by such services.

To address this issue, Undetected GeckoDriver acts as an interface between your code and Selenium, helping you bypass bot detection mechanisms. When you create a new WebDriver instance using the `Firefox()` class from the Undetected GeckoDriver package (as opposed to using Selenium directly), the following processes occur:

1. The original Firefox binary is located, copied, and patched to prevent it from modifying properties such as `navigator.webdriver` while using Selenium.
2. A Selenium WebDriver instance is created that uses the patched Firefox binary.

This makes it possible to interact with websites without being detected as a bot, allowing you to scrape data, automate tasks, and perform other browser-based operations without triggering bot detection mechanisms.

## Installation

You can install the package via pip:

```bash
pip install undetected-geckodriver
```

Or you can install it from source:

```bash
git clone https://github.com/bytexenon/undetected_geckodriver
cd undetected_geckodriver
pip install .
```

> [!NOTE]
> The last installation method is not recommended unless you are planning to contribute to the project. For regular usage, it is recommended to install the package via regular pip installation.

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
   search_box = driver.find_element(By.NAME, "q")
   search_box.send_keys(SEARCH_FOR)
   search_box.submit()

   # Wait for the page to load
   time.sleep(2)

   # Print the current URL after the search
   print("Current URL:", driver.current_url)

   # Wait for a while to observe the results
   time.sleep(15)

   # Ensure the browser is closed
   driver.quit() # Close the browser
   ```

For further information and advanced usage, you can take a look at the [official Selenium documentation](https://www.selenium.dev/documentation/en/) since Undetected GeckoDriver is built on top of Selenium.

## Requirements

- **`Firefox`**
- **`Python >= 3.6`**
- **`Selenium >= 4.10.0`**
- **`Psutil >= 5.8.0`**

## FAQ

### The browser is still being detected as a bot. What should I do?

If your browser is still being detected as a bot while using Undetected GeckoDriver, it may be due to advanced bot detection mechanisms on the website. In such cases, please open an issue on the GitHub repository with the website URL and any relevant information. This will help in investigating and potentially adding support for it in future releases.

### Why patch the Firefox binary?

When Firefox is controlled remotely by a script (such as when using Selenium), it sets certain properties that can be detected by anti-bot services as defined in the WebDriver specification. Selenium itself doesn't control these properties directly. By patching the Firefox binary, we can prevent it from modifying these properties, allowing us to interact with websites without being detected as a bot.

### Why use Undetected GeckoDriver over undetected-chromedriver?

While undetected-chromedriver is a great tool for bypassing bot detection mechanisms, it only supports Chrome and Edge browsers. Undetected GeckoDriver fills this gap by providing similar functionality for Firefox browsers.

## Roadmap

**Completed:**

- [x] **Spoof `navigator.webdriver` property**: Implement a method to spoof the `navigator.webdriver` property to prevent detection by services like Cloudflare. This helps in avoiding bot detection mechanisms.

**In Progress:**

- [ ] **Multi-platform support**: Extend the compatibility of the tool to work seamlessly across different operating systems other than Linux (Windows, macOS). This includes ensuring all dependencies and configurations are platform-independent.

**Planned:**

- [ ] **Helper functions for passing CAPTCHAs and other security measures**: Develop utility functions to automate the solving of CAPTCHAs and bypass other common security measures encountered during web scraping. (e.g. automatically passing Cloudflare's "I'm human" challenge)

- [ ] **Support for Selenium Wire**: Integrate Selenium Wire to allow for more advanced network interactions, such as modifying requests and responses.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request if you encounter any problems or have any suggestions, improvements, or new features you would like to see implemented.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Special thanks to the contributors of the Selenium project.
- Inspiration from the [undetected-chromedriver project](https://github.com/ultrafunkamsterdam/undetected-chromedriver).
