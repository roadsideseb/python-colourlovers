from distutils.core import setup
import sys

import colourlovers 

setup(
    name='python-colourlovers',
    version='0.1',
    author='Sebastian Vetter',
    author_email='sebastian@roadside-developer.com',
    url='http://python-colourlovers.readthedocs.org',
    #download_url='https://sourceforge.net/projects/py-googlemaps/files/',
    description='An API providing access to the ColourLovers website.',
    long_description=colourlovers.__doc__,

    packages = [
        'colourlovers', 
    ],

    provides = ['colourlovers'],
    license='GNU General Public License (GPL)',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
