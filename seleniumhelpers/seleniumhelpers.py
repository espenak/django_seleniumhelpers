from selenium.webdriver.support.ui import WebDriverWait
from unittest import skipIf
from django.test import LiveServerTestCase
import os

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from django.conf import settings


def get_setting_with_envfallback(setting, default=False):
    return getattr(settings, 'SKIP_SELENIUMTESTS', os.environ.get('SKIP_SELENIUMTESTS', default))

@skipIf(get_setting_with_envfallback('SKIP_SELENIUMTESTS'),
    'Selenium tests have been disabled in settings.py using SKIP_SELENIUMTESTS=True.')
class SeleniumTestCase(LiveServerTestCase):
    @classmethod
    def getDriver(self):
        browser = get_setting_with_envfallback('SELENIUM_BROWSER', 'Chrome')
        return getattr(webdriver, browser)()

    @classmethod
    def setUpClass(cls):
        cls.selenium = cls.getDriver()
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

    def waitForCssSelector(self, cssselector, timeout=10):
        """
        Wait for the given ``cssselector``.

        :param timeout: Fail unless the ``cssselector`` is found before ``timeout`` seconds. Defaults to ``10``.
        """
        WebDriverWait(self.selenium, timeout).until(lambda selenium: selenium.find_elements_by_css_selector(cssselector))

    def waitForEnabled(self, element, timeout=10):
        """
        Wait for the given ``element`` to become enabled (``element.is_enabled() == True``).

        :param timeout: Fail unless the ``element`` becomes enabled before ``timeout`` seconds. Defaults to ``10``.
        """
        WebDriverWait(self.selenium, timeout).until(lambda selenium: element.is_enabled())

    def waitForText(self, text, timeout=10):
        """
        Wait for ``text`` to appear in ``selenium.page_source``.

        :param timeout: Fail unless the ``text`` appears in ``selenium.page_source`` before ``timeout`` seconds has passed. Defaults to ``10``.
        """
        WebDriverWait(self.selenium, timeout).until(lambda selenium: text in selenium.page_source)

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

    def waitFor(self, item, fn, timeout=10):
        """
        Wait for the ``fn`` function to return ``True``. The ``item`` is
        forwarded as argument to ``fn``.

        Example (wait for text in an element)::

            waitFor(myelem, lambda myelem: len(myelem.text) > 0)
        """
        WebDriverWait(item, timeout).until(fn)

    def failIfCssSelectorFound(self, element, css_selector):
        """
        Assert that ``element.find_element_by_css_selector(css_selector)``
        raises ``NoSuchElementException``.
        """
        with self.assertRaises(NoSuchElementException):
            element.find_element_by_css_selector(css_selector)
