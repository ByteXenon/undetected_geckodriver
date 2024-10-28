# Constants #
TO_REPLACE_STRING = b"webdriver"

PLATFORM_DEPENDENT_PARAMS = {
    # Do not remove, the (actual) support for Windows & macOS is coming soon
    # "Windows": {
    #    "firefox_execs": ["firefox.exe"],
    #    "firefox_paths": ["C:\\Program Files\\Mozilla Firefox"],
    #    "undetected_path": "C:\\Users\\{USER}\\AppData\\Local\\undetected_firefox\\",
    #    "xul": "xul.dll",
    # },
    # "Darwin": {
    #    "firefox_execs": ["Firefox.app"],
    #    "firefox_paths": ["/Applications/Firefox.app/Contents/MacOS"],
    #    "undetected_path": "/Users/{USER}/Library/Caches/undetected_firefox/",
    #    "xul": "libxul.dylib",
    # },
    "Linux": {
        "firefox_execs": ["firefox", "firefox-bin"],
        "firefox_paths": [
            "/usr/lib/firefox",
            "/usr/lib/firefox-esr",
            "/usr/lib/firefox-developer-edition",
            "/usr/lib/firefox-nightly",
            "/usr/lib/firefox-trunk",
            "/usr/lib/firefox-beta",
        ],
        "undetected_path": "/home/{USER}/.cache/undetected_firefox/",
        "xul": "libxul.so",
    },
}
