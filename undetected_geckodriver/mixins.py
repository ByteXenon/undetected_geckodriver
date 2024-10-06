class WebDriverMixin:
    def __getattr__(self, attr):
        return getattr(self.webdriver, attr)

    def __getitem__(self, key):
        return self.webdriver[key]

    def __setitem__(self, key, value):
        self.webdriver[key] = value

    def __delitem__(self, key):
        del self.webdriver[key]

    def __iter__(self):
        return iter(self.webdriver)

    def __len__(self):
        return len(self.webdriver)

    def __type__(self):
        return type(self.webdriver)

    def __str__(self):
        return str(self.webdriver)
