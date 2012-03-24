#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# python-colourlovers - A Python API to http://www.colourlovers.com 
# Copyright (C) 2012 Sebastian Vetter
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License

from distutils.core import setup


setup(
    name = 'python-colourlovers',
    version = '0.0.1',
    author = 'Sebastian Vetter',
    author_email = 'sebastian@roadside-developer.com',
    url = 'http://python-colourlovers.readthedocs.org',

    description = 'An API providing access to the ColourLovers website.',
    long_description = open('README.rst', 'r').read(),

    packages = [
        'colourlovers', 
    ],

    provides = ['colourlovers'],
    license = 'GNU General Public License (GPL)',

    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Environment :: Web Environment',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: POSIX',
        'Operating System :: OS Independent',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
