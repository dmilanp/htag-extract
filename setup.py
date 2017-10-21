#!/usr/bin/env python
from distutils.core import setup

reqs = [
    'beautifulsoup4==4.5.3',
    'requests==2.13.0',
]

setup(
    name='htag-extract',
    version='1.0',
    description='HTML tag extractor',
    author='Diego Milan',
    author_email='ddmilanpp@gmail.com',
    scripts=['html'],
    install_requires=reqs
)