.. _phantomjs:
===============================
PhantomJS
===============================

We support PhantomJS via ghostdriver.


Requirements
------------
You need to build PhantomJS as described on the `ghostdriver website <https://github.com/detro/ghostdriver>`_.


Running tests with PhantomJS and ghostdriver
--------------------------------------------

Run PhantomJS with ghostdriver on port ``8080`` as described on the ghostdriver website::

    $ phantomjs /path/to/ghostdriver/src/main.js 8080

Run the tests with ``SELENIUM_BROWSER=phantomjs``::

    SELENIUM_BROWSER=phantomjs python manage.py test
