from django.core.management.base import BaseCommand

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


class Command(BaseCommand):
    help = 'List possible SELENIUM_BROWSER\'s.'
    def handle(self, *args, **options):
        for attrname in dir(webdriver):
            attr = getattr(webdriver, attrname)
            try:
                if issubclass(attr, WebDriver):
                    print '-', attrname
            except TypeError:
                pass # attr is not a class
