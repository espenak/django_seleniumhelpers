from unittest import skipIf
import os
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from django.test import LiveServerTestCase


def get_setting_with_envfallback(setting, default=None, typecast=None):
    try:
        from django.conf import settings
    except ImportError:
        return default
    else:
        fallback = getattr(settings, setting, default)
        value = os.environ.get(setting, fallback)
        if typecast:
            value = typecast(value)
        return value

def get_default_timeout():
    return get_setting_with_envfallback('SELENIUM_DEFAULT_TIMEOUT', default=4,
                                        typecast=int)


@skipIf(get_setting_with_envfallback('SKIP_SELENIUMTESTS'),
    'Selenium tests have been disabled in settings.py using SKIP_SELENIUMTESTS=True.')
class SeleniumTestCase(LiveServerTestCase):
    """
    Extends ``django.test.LiveServerTestCase`` to simplify selenium testing.
    """
    @classmethod
    def _getDriver(self):
        browser = get_setting_with_envfallback('SELENIUM_BROWSER', 'Chrome')
        return getattr(webdriver, browser)()

    @classmethod
    def setUpClass(cls):
        """
        Adds the ``selenium`` attribute to the class. The ``selenium`` attribute
        defaults to an instance of ``selenium.webdriver.Chrome``, however this
        can be overridden using the ``SELENIUM_BROWSER`` django setting or environment
        variable. If both the django setting and and environment variable is set, the
        environment variable is used. This means that you can set the default
        value in ``settings.py`` and override it in an environment variable, typically
        when running the ``test`` command::

            SELENIUM_BROWSER=Firefox python manage.py test
        """

        #: The selenium testbrowser object.
        cls.selenium = cls._getDriver()

        super(SeleniumTestCase, cls).setUpClass()

    @classmethod
    def tearDownClass(cls):
        super(SeleniumTestCase, cls).tearDownClass()
        cls.selenium.quit()


    def getPath(self, path):
        """
        Shortcut for ``self.selenium.get(...)`` with ``path`` prefixed by
        ``live_server_url`` as argument.
        """
        return self.selenium.get('{live_server_url}{path}'.format(live_server_url=self.live_server_url,
                                                                path=path))

    def waitForCssSelector(self, cssselector,
                           timeout=get_default_timeout(),
                           within=None, msg='No elements match css selector "{cssselector}".'):
        """
        Wait for the given ``cssselector``.

        :param within: The element to run ``find_element_by_css_selector()`` on. Defaults to ``self.selenium``.
        :param timeout: Fail unless the ``cssselector`` is found before ``timeout`` seconds.
        """
        within = within or self.selenium
        self.waitFor(within,
                     lambda e: e.find_elements_by_css_selector(cssselector),
                     timeout=timeout,
                     msg=msg.format(cssselector=cssselector))

    def waitForCssSelectorNotFound(self, cssselector,
                                   timeout=get_default_timeout(),
                                   within=None,
                                   msg='CSS selector, "{cssselector}" matches at least one element, when we expected it not to.'):
        """
        Wait for the given ``cssselector`` not to be found.

        :param within: The element to run ``find_elements_by_css_selector()`` on. Defaults to ``self.selenium``.
        :param timeout: Fail if the ``cssselector`` is still found after ``timeout`` seconds.
        """
        within = within or self.selenium
        self.waitFor(within,
                     lambda e: len(e.find_elements_by_css_selector(cssselector)) == 0,
                     timeout=timeout,
                     msg=msg.format(cssselector=cssselector))

    def waitForEnabled(self, element,
                       timeout=get_default_timeout(),
                       msg='The element is not enabled.'):
        """
        Wait for the given ``element`` to become enabled (``element.is_enabled() == True``).

        :param timeout: Fail unless the ``element`` becomes enabled before ``timeout`` seconds.
        """
        self.waitFor(self.selenium, lambda selenium: element.is_enabled(),
                     timeout, msg)

    def waitForDisabled(self, element,
                        timeout=get_default_timeout(),
                        msg='The element is not disabled.'):
        """
        Wait for the given ``element`` to become disabled (``element.is_enabled() == False``).

        :param timeout: Fail unless the ``element`` becomes disabled before ``timeout`` seconds. Defaults to ``10``.
        """
        self.waitFor(self.selenium, lambda selenium: not element.is_enabled(),
                     timeout, msg)

    def waitForText(self, text,
                    timeout=get_default_timeout(),
                    msg='Could not find text "{text}"'):
        """
        Wait for ``text`` to appear in ``selenium.page_source``.

        :param timeout: Fail unless the ``text`` appears in ``selenium.page_source`` before ``timeout`` seconds has passed.
        """
        self.waitFor(self.selenium, lambda selenium: text in selenium.page_source, timeout,
                     msg=msg.format(text=text))

    def waitForTitle(self, title,
                     timeout=get_default_timeout()):
        """
        Wait until the page title (title-tag) equals the given ``title``.
        """
        self.waitFor(self.selenium, lambda selenium: selenium.title==title,
                     timeout=timeout,
                     msg='Title does not contain "{title}"'.format(**vars()))

    def waitForTitleContains(self, title,
                             timeout=get_default_timeout()):
        """
        Wait until the page title (title-tag) contains the given ``title``.
        """
        self.waitFor(self.selenium, lambda selenium: title in selenium.title,
                     timeout=timeout,
                     msg='Title does not contain "{title}"'.format(**vars()))

    def executeScript(self, script, element):
        """
        Shortcut for ``self.selenium.executeScript(script, element)``.
        """
        return self.selenium.execute_script(script, element)

    def getInnerHtml(self, element):
        """
        Get ``innerHTML`` of the given element.
        """
        return self.executeScript("return arguments[0].innerHTML", element)

    def waitFor(self, item, fn,
                timeout=get_default_timeout(),
          msg=None):
        """
        Wait for the ``fn`` function to return ``True``. The ``item`` is
        forwarded as argument to ``fn``.

        Example (wait for text in an element)::

            waitFor(myelem, lambda myelem: len(myelem.text) > 0, msg='myelem is empty')
        """
        try:
            WebDriverWait(item, timeout).until(fn)
        except TimeoutException, e:
            errormessage = 'waitFor timed out after {timeout} seconds. Error message: {msg}'.format(**vars())
            self.fail(errormessage)

    def failIfCssSelectorFound(self, element, css_selector,
                               msg='CSS selector, "{css_selector}" matches at least one element, when we expected it not to.'):
        """
        Assert that ``element.find_element_by_css_selector(css_selector)``
        raises ``NoSuchElementException``.
        """
        try:
            element.find_element_by_css_selector(css_selector)
        except NoSuchElementException, e:
            self.fail(msg=msg.format(css_selector=css_selector))
