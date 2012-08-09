import codecs
import os
import sys
from setuptools import setup, find_packages

def read(fname):
    return codecs.open(os.path.join(os.path.dirname(__file__), fname)).read()

PACKAGE = "portfolio"
NAME = "django-folio"
DESCRIPTION = "A reusable Django app for displaying a portfolio of your work"
AUTHOR = "Chris Clarke"
AUTHOR_EMAIL = "cclarke@chrisdev.com"
URL = "http://github.com/chrisdev/django-folio"

VERSION = __import__(PACKAGE).__version__

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=read('README.rst'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 1  - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)

