#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

setup(
    name = "django-redirect",
    version = "0.1",
    url = 'http://github.com/glenbot/django-redirect',
    download_url = 'http://github.com/glenbot/django-redirect/tarball/master',
    license = 'GPL',
    description = "A slightly more robust version of the native django redirect.",
    author = 'Glen Zangirolami',
    author_email = 'glenbot@gmail.com',
    packages = find_packages(),
    namespace_packages = ['redirect'],
    include_package_data = True,
    zip_safe = False,
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: GPL License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ]
)
