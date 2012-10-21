=====
Usage
=====

Subclass :class:`seleniumhelpers.SeleniumTestCase` instead of
``django.test.LiveServerTestCase`` in your testcases.

Example
-------

::

    from seleniumhelpers import SeleniumTestCase

    class TestFrontpage(SeleniumTestCase):
        def test_frontpageimage(self):
            # Use our shortcut instead of self.selenium.get(self.live_server_url + '/something')
            self.getPath('/something/')

            # Fail unless the expected image and text is available within 10 secons
            self.waitForCssSelector('img.frontpageimage')
            self.waitForText(u'This is the frontpage image text.')

            # Assert that we remembered to close the body. Mostly to show how
            # to get hold of the selenium WebDriver object
            # Note: The selenium attribute is actually set as an attribute on
            #       the class in SeleniumTestCase.setUpClass()
            self.assertTrue('</body>' in self.selenium.page_source)
            


Running tests
-------------

You can run the tests just like normal Django tests, however we provide the ability to override 
the browser used for the tests, and to completely skip all selenium tests.

Select selenium browser::

    $ SELENIUM_BROWSER=Firefox python manage.py test

See available browsers::

    $ python manage.py listseleniumbrowsers

Skip selenium tests::

    $ SKIP_SELENIUMTESTS=1 python manage.py test

.. note::
    Settings can also be set in ``settings.py``. See :ref:`settings`.


Configure timout
----------------

You can configure the default timeout using ``SELENIUM_DEFAULT_TIMEOUT``, in
``settings.py`` or as environment variables, just like ``SKIP_SELENIUMTESTS``
and ``SELENIUM_BROWSER``. Example::

    $ SELENIUM_BROWSER=Firefox SELENIUM_DEFAULT_TIMEOUT=10 python manage.py test

The default timeout is ``4`` seconds, which should be enough unless you are
running on a very slow machine.



Use Selenium RC
---------------
Using Selenium RC is easy, it only requires you to run the RC-server, and use an additional setting:

1. Download _selenium-server-standalone-XXXX.jar_ from http://code.google.com/p/selenium/downloads/list.
2. Run the RC-server::

    $ java -jar selenium-server-standalone-XXXX.jar

3. Run the tests with SELENIUM_USE_RC::

    $ SELENIUM_USE_RC=true SELENIUM_BROWSER=Opera python manage.py test


SeleniumTestCase API docs
-------------------------

.. autoclass:: seleniumhelpers.SeleniumTestCase
    :members:
