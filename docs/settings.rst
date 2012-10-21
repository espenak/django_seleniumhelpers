.. _settings:
===============================
Settings
===============================


All the settings can be set in ``settings.py``, and most settings can be set
through using environment variables. If a setting is both in ``settings.py``
and as an environment variable, the environment variable is used.


List of settings
----------------

SKIP_SELENIUMTESTS
    Skip all seleniumtests.
SELENIUM_BROWSER
    The selenium browser to use. Defaults to ``Chrome``.
SELENIUM_USE_RC
    If ``bool(SELENIUM_USE_RC)`` is ``True``, we use the Selenium RC server
    instead of webdriver to run the tests. ``SELENIUM_BROWSER`` is forwarded to
    the RC-server as the browser.
SELENIUM_DEFAULT_TIMEOUT
    The default timeout, in seconds, of the ``waitFor*`` methods. Defaults to ``4``.
