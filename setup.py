#!/usr/bin/env python
from setuptools import setup, find_packages
import os
import rest_framework_utils

def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(name='django-rest-framework-utils',
    version=rest_framework_utils.__version__,
    description='Miscellaneous utilities built on top of Django Rest framework',
    author='Carlos Arrastia',
    author_email='carlos.arrastia@gmail.com',
    packages=['rest_framework_utils',
              'rest_framework_utils.views',
              'rest_framework_utils.fields',
              'rest_framework_utils.permissions',
              ],
    keywords='python django rest_framework rest',
    license='MIT',
    include_package_data=True,
    # http://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
    install_requires=[
        "djangorestframework" >= "2.3.8", # it might still work in a lower version
    ],
    extras_require=[
        "requests" >= "2.2.0",
        "django-taggit" >= "0.9.0",
    ]
)
