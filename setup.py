from os.path import join, dirname
from setuptools import setup, find_packages

this_dir = dirname(__file__)

try:
    f = open(join(this_dir, 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(name = 'django_seleniumhelpers',
      description = 'Extends django.test.LiveServerTestCase to make selenium testing even easier.',
      version = '1.0',
      license='BSD',
      url = 'https://github.com/espenak/django_seleniumhelpers',
      author = 'Espen Angell Kristiansen',
      packages=find_packages(exclude=['ez_setup']),
      install_requires = ['setuptools', 'Django'],
      include_package_data=True,
      zip_safe=False,
      classifiers=[
                   'Development Status :: 5 - Production/Stable',
                   'Environment :: Web Environment',
                   'Framework :: Django',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python'
                  ]
)
