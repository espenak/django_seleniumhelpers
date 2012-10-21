==============================================
Customize the driver-object (cls.selenium)
==============================================

The ``selenium``-attribute of the :class:`seleniumhelpers.SeleniumTestCase`` is
created in the :meth:`seleniumhelpers.SeleniumTestCase.getDriver` classmethod.
You can override this method if you have more advanced needs than the simple
customizations provided by the default implementation.

Example
-------
This example makes it possible to run Firefox3.6 if ``SELENIUM_BROWSER=="Firefox3.6"``::

    from seleniumhelpers import SeleniumTestCase

    class CustomSeleniumTestCase(SeleniumTestCase):
        @classmethod
        def getDriver(cls, browser, use_rc):
            if browser == 'Firefox3.6':
                return webdriver.Remote('desired_capabilities': {'browser_name': browser,
                                                                 'version': '3.6'})
            else:
                return super(CustomSeleniumTestCase, self).getDriver(browser, use_rc)
