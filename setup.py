from distutils.core import setup

import colourlovers 

setup(
    name = 'python-colourlovers',
    version = '0.1.0',
    author = 'Sebastian Vetter',
    author_email = 'sebastian@roadside-developer.com',
    url = 'http://python-colourlovers.readthedocs.org',

    description = 'An API providing access to the ColourLovers website.',
    long_description = colourlovers.__doc__,

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
    ]
)
