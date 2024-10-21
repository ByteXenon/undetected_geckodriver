# Imports #
import os

from selenium.webdriver.common.driver_finder import DriverFinder
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.remote_connection import FirefoxRemoteConnection
from selenium.webdriver.firefox.service import Service

from .mixins import WebDriverMixin
from .utils  import (
    get_webdriver_instance,
    get_firefox_installation_path,
    create_undetected_firefox_directory,
    get_undetected_firefox_path,
    patch_libxul_file,
    _get_platform_dependent_params
)

# Main class #
class Firefox(RemoteWebDriver, WebDriverMixin):
    """
    A custom Firefox WebDriver that attempts to avoid detection by web services.
    """

    def __init__(
        self, options: Options = None, service: Service = None, keep_alive: bool = True
    ) -> None:
        self.webdriver = get_webdriver_instance()

        self._firefox_path = get_firefox_installation_path()
        self._undetected_path = get_undetected_firefox_path()

        create_undetected_firefox_directory(self._firefox_path, self._undetected_path)
        patch_libxul_file(self._undetected_path)

        self.service = service if service else Service()
        options = options if options else Options()
        options.binary_location = os.path.join(self._undetected_path, _get_platform_dependent_params()["firefox_exec"])

        finder = DriverFinder(self.service, options)

        self.service.path = finder.get_driver_path()
        self.service.start()

        executor = FirefoxRemoteConnection(
            remote_server_addr=self.service.service_url,
            keep_alive=keep_alive,
            ignore_proxy=options._ignore_local_proxy,
        )
        try:
            super().__init__(command_executor=executor, options=options)
        except Exception:
            self.quit()
            raise
        self._is_remote = False
