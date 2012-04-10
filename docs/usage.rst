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

    $ SELENIUM_BROWSER=Firefox python manage.py listseleniumbrowsers

Skip selenium tests::

    $ SKIP_SELENIUMTESTS=1 python manage.py test

.. note::

    ``SKIP_SELENIUMTESTS`` and ``SELENIUM_BROWSER`` may also be set in
    ``settings.py``. See :meth:`seleniumhelpers.SeleniumTestCase.setUpClass`
    for more details.




SeleniumTestCase API docs
-------------------------

.. autoclass:: seleniumhelpers.SeleniumTestCase
    :members:
