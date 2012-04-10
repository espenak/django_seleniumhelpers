.. django_seleniumhelpers documentation master file, created by
   sphinx-quickstart on Tue Apr 10 18:20:56 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to django_seleniumhelpers's documentation!
==================================================

Contents:

.. toctree::
   :maxdepth: 2


Getting started
===============

Features
--------

- Skip selenium tests
- Select test browser
- Helper functions to simplify common use cases.


Issues/contribute
-----------------

Report any issues at the `github project page <django_seleniumhelpers>`_, and feel free
to add your own guides/experiences to the wiki, and to contribute changes using
pull requests.


Install
-------

Requires **django>=1.4**.

::

    $ pip install django_seleniumhelpers


Setup
-----

Add ``'seleniumhelpers'`` to ``INSTALLED_APPS``.


.. _`django_seleniumhelpers`: https://github.com/espenak/django_seleniumhelpers



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
            self.getPath('/something/')
            # Fail unless the expected image and text is available within 10 secons
            self.waitForCssSelector('img.frontpageimage')
            self.waitForText(u'This is the frontpage image text.')


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


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

