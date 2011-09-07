
class SeleniumContext():
    """Class to run code into some Selenium-related context, i.e. with some
    browser."""
    def __init__(self):
        self._browser = []

    def get_browser(self):
        return self._browser[-1]

    def push_browser(self, browser):
        self._browser.append(browser)

    def pop_browser(self):
        browser = self._browser.pop()
        browser.close()
        return browser

    def with_browsers(self, func, browser_callables, *args, **kwargs):
        """Decorator that runs the given method with several browsers."""
        for (b_callable, b_args, b_kwargs) in browser_callables:
            browser = b_callable(*b_args, **b_kwargs)
            self.push_browser(browser)
            func(*args, **kwargs)
            self.pop_browser()
