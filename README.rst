################
Selenium context
################

.. note:: This project is experimental! Concept has not been proved yet.

This project provides utilities to write and run generic Selenium tests in
several environments:

* write generic Selenium tests, not tied to specific browsers, web servers or
  selenium server/rc/grid.
* during deployment, configure your Selenium environment: which browsers are
  available, what is the base URL of your development server, ...
* with one command, run Selenium tests with all the browsers available in your
  environment.

****************
Running the demo
****************

This project provides a demo in the demo/ folder.
See demo/README.rst for details.

*****
Story
*****

Let's consider the code provided at
http://seleniumhq.org/docs/03_webdriver.html#id4

* I'm running Linux, I got Firefox. I wrote the TestCase described above.
  ::

    from selenium import webdriver
    from selenium.common.exceptions import TimeoutException
    from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
    import time

    # Create a new instance of the Firefox driver
    driver = webdriver.Firefox()

    # go to the google home page
    driver.get("http://www.google.com")

    # find the element that's name attribute is q (the google search box)
    inputElement = driver.find_element_by_name("q")

    # type in the search
    inputElement.send_keys("Cheese!")

    # submit the form (although google automatically searches now without submitting)
    inputElement.submit()

    # the page is ajaxy so the title is originally this:
    print driver.title

    try:
        # we have to wait for the page to refresh, the last thing that seems to be updated is the title
        WebDriverWait(driver, 10).until(lambda driver : driver.title.lower().startswith("cheese!"))

        # You should see "cheese! - Google Search"
        print driver.title

    finally:
        driver.quit()

* One of my colleagues uses Safari. He can't run the test (and does not want
  Firefox on his system!). Does he change the test source code to use Safari?
  It's so bad!
* I also got Chrome on my system and, guess what, I want it to be tested too.
  Do I duplicate the test to support Chrome?
* ... and my colleague duplicates to support Safari? By the way, it will fail
  on my system!
* Oh! My sysadmin installed some Selenium Grid, how to tell the continuous
  integration server that he can run tests with IE too?
* On my development machine, I run Selenium tests on my development server, at
  http://127.0.0.1 but the continuous build server runs tests at
  http://integration.example.com/... so I don't want hardcoded base URL!
* I am using webdriver to control a Firefox on my own machine, I don't need a
  Selenium server. But the continuous build server uses a Selenium Grid... so
  I don't want the Selenium server's URL to be hardcoded!
* I want to write generic tests!
* I want to configure my environment!
* I want a test runner that runs tests with all available environments (at
  least with all available browsers)!

********
Workflow
********

Running tests (deploy)
======================

Let's say tests are already written.

* Get a Selenium environment (selenium webdriver, selenium, seleniumrc,
  selenium grid...).
* Configure local Selenium environment settings:

  * browsers list (typically, those installed on your system)
  * base URL to run tests (typically, URL of your development/integration web
    server)
  * optionnally, URL of remote Selenium server (Selenium RC or Selenium Grid)
  * optionnally, command/recipe to start web server
  * optionnally, command/recipe to start Selenium environment

* Run tests, i.e. launch some Selenium tests with all available browsers

Writing tests (develop)
=======================

* Add dependency to the "Selenium context" library
* When tests are not browser specific, use/inherit the global/default Selenium
  context. The global/default Selenium context will be initialized by the test
  runner. If there are several browsers available, the test runner will launch
  the tests several times, each time with a different Selenium context.
* When tests are browser specific (i.e. you need to validate something specific
  to IE), use a local context.

**************
Implementation
**************

* SeleniumContext class
* push/pop system. Makes it possible to change current context temporarily and
  restore it.
* decorator for test methods? Is it possible to decorate TestCase methods like
  this?
  ::

    @with_browsers((webdriver.browsers.Firefox, webdriver.browsers.Chrome))
    def test_something_specific_to_firefox_and_chrome(self, context=None):
        browser = context.get_browser()
        browser.get(context.base_url)

* SeleniumContextManager singleton? So that we can effectively use something
  like:
  ::

    browser = SeleniumContextManager.get_browser()

* TestCase.selenium_context property? So that we can effectively use something
  like:
  ::

    browser = self.selenium_context.get_browser()

* URL utilities?
  ::

    # Somewhere in local configuration...
    selenium_context.base_url = 'http://www.example.com/'

    # Somewhere in tests...
    # browser.get() expects an absolute URL...
    # ... but we don't have a fixed base URL here since it is a setting.
    # So we have to dynamically construct the absolute URL.
    browser.get(selenium_context.url('/some/url/that/is/relative/to/base/url'))

*****
Notes
*****

Have a look at the following packages on pypi:

* selenium
* collective.recipe.seleniumrc or rcom.recipe.seleniumenv
* gocept.selenium

Multiple browsers in the same environment?

* as a developer, I can run several browsers on my own machine
* a Selenium grid can run several browsers

The main questions this package tries to address are:

* how can I run tests with several browsers?
* how can I run tests on not-Python web servers? What if I cannot start the
  (dev) server with Python standards (i.e. not a wsgi server)
* how can I run tests which are not using a particular framework? As an example
  I would like to run Python Selenium tests on some external website, I don't
  even develop the website, so I don't use a framework!

Running Selenium tests means:

* install SeleniumRC if necessary
* run Selenium if necessary
* connect to an existing Selenium server
* run the web server on which run tests if necessary
* connect to the web server
* find Selenium tests
* execute them for each available browser
* stop servers if necessary

Running Chrome:

* you need chromium webdriver to be able to run chrome (at least on linux), but
  it is in the docs...
