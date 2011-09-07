from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

from seleniumcontext import SeleniumContext


class IndexTestCase(unittest.TestCase):
    def setUp(self):
        self.selenium_context = SeleniumContext()
        #remote = None
        #capabilities = DesiredCapabilities.FIREFOX
        #profile = None
        #if remote:
        #    self.browser = webdriver.Remote(remote, capabilities, profile)
        #else:
        #    self.browser = webdriver.Firefox()
        #self.verificationErrors = []

    
#    def _test_with_browsers(self, method):
#        """Utility method that launch another method with several browsers.
#
#        TODO: make it a decorator???
#        """
#        browser_callables = (
#            
#        )
#        for (browser_callable, args) in browser_callables:
#            self.browser = browser_callable(*args)
#            method()
#            self.browser.close()

    def _test_page_loading(self):
        browser = self.selenium_context.get_browser()
        browser.get("https://bitbucket.org/benoitbryon")

    def test_page_loading(self):
        """A very simple testcase: loads / URL. This is a proof-of-concept 
        test.
        """
        self.selenium_context.with_browsers(self._test_page_loading, ((webdriver.Firefox, [], {}), (webdriver.Chrome, [], {})))
    
    def tearDown(self):
        #self.assertEqual([], self.verificationErrors)
        #self.browser.close()
        pass
