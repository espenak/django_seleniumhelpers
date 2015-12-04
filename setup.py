from setuptools import setup, find_packages

setup(name = 'django_seleniumhelpers',
      description = 'Extends django.test.LiveServerTestCase to make selenium testing even easier.',
      version = '1.1.2',
      license='BSD',
      url = 'https://github.com/espenak/django_seleniumhelpers',
      author = 'Espen Angell Kristiansen',
      author_email = 'post@espenak.net',
      packages=find_packages(exclude=['ez_setup']),
      install_requires = ['distribute', 'Django', 'selenium'],
      include_package_data=True,
      zip_safe=False,
      long_description='See http://github.com/espenak/django_seleniumhelpers',
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
