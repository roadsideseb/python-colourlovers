The ColourLovers Python API
===========================

.. image:: https://travis-ci.org/elbaschid/python-colourlovers.png?branch=master
    :target: https://travis-ci.org/elbaschid/python-colourlovers

.. image:: https://img.shields.io/pypi/v/python-colourlovers.svg
    :target: https://crate.io/packages/python-colourlovers/

.. image:: https://img.shields.io/pypi/dm/python-colourlovers.svg
    :target: https://crate.io/packages/python-colourlovers/


This Python package ``python-colourlovers`` access to the ColourLovers.com
API, a web service that allows users to publish colour themes and rate them.
The API of this webservice allows to search for users (Lovers) and their
posted contents (Colours, Patterns, Palettes).

Accessing the API requires an instance of ``ColourLovers``
which provides the methods to access the different content types:
*Colour*, *Palette*, *Pattern*, *Lover*. Sending a request to
ColourLovers is as easy as calling the corresponding method such as
``ColourLovers.palettes()`` to search for palettes.
Additionally, the following arguments can be specified ``new``, ``top``,
``random`` with additional parameters. Please refer to the ColourLovers
API documentation to find out more about the specific parameters and
their restrictions at http://www.colourlovers.com/api.

You find the ColourLovers website at: http://www.colourlovers.com

The ColourLovers.com API is provided under the Creative Commons
**Attribution-Noncommercial-Share Alike** license. Please refer to
http://www.colourlovers.com/api for more information on the license
and Terms Of Use.

You find the source code and the latest development version on github:
https://github.com/elbaschid/python-colourlovers. That's also the place
where you can leave feedback and contribute your own code. Just fork the
repo, make your changes and send me a pull request :)


Colours
-------

The ColourLovers.com API provides two different ways to retrieve a
colour or a list of colours.

1. Searching for a single colour by calling the ``ColourLovers.color()``
   method with the desired colour's hexcode, e.g. ``#37cbff``. This will
   return the corresponding colour as ``ColourLovers.Colour`` instance.
2. Searching  for multiple colours by calling ``ColourLovers.colours()``
   with one of these arguments: ``new``, ``top``, ``random``. This will
   return a list of ``ColourLovers.Colour`` objects.

For details on additional parameters please refer to the documentation at
http://python-colourlovers.readthedocs.org

Example::

    >>> from colourlovers import ColourLovers
    >>> cl = ColourLovers()
    >>> cl.color('#37cbff')
    [<Colour id='4767129' title='i feel pretty' rgb=(55, 203, 255)>]
    >>> cl.palettes('new', keywords='funky', numResults=3)
    [<Palette id='1940972' title='"Funky President"'>,
     <Palette id='1936394' title='Barbie Doll Blonde'>,
     <Palette id='1936247' title='Lily's Rainbow'>]

Palettes
--------

The ColourLovers.com API provides two different ways to retrieve a
palette or a list of palettes:

1. Searching for a single palette by calling the ``ColourLovers.palette()``
   method with the desired palette ID, e.g. ``1942043``. This will
   return the corresponding colour as ``ColourLovers.Palette`` instance.
2. Searching  for multiple palettes by calling ``ColourLovers.palettes()``
   with one of these arguments: ``new``, ``top``, ``random``. This will
   return a list of ``ColourLovers.Palette`` objects.

For details on additional parameters please refer to the documentation at
http://python-colourlovers.readthedocs.org

Example::

    >>> from colourlovers import ColourLovers
    >>> cl = ColourLovers()
    >>> cl.palettes('random')
    [<Palette id='114699' title='chunky butt'>]
    >>> cl.palette(1942043)
    [<Palette id='1942043' title='Drinking Game 2'>]

Patterns
--------

The ColourLovers.com API provides two different ways to retrieve a
pattern or a list of patterns.

1. Searching for a single pattern by calling the ``ColourLovers.pattern()``
   method with the desired pattern's ID, e.g. ``2111513``. This will
   return the corresponding pattern as ``ColourLovers.Pattern`` instance.
2. Searching  for multiple patterns by calling ``ColourLovers.patterns()``
   with one of these arguments: ``new``, ``top``, ``random``. This will
   return a list of ``ColourLovers.Pattern`` objects.

For details on additional parameters please refer to the documentation at
http://python-colourlovers.readthedocs.org

Example::

    >>> from colourlovers import ColourLovers
    >>> cl = ColourLovers()
    >>> cl.patterns('random')
    [<Pattern id='391644' title='acanalado'>]
    >>> cl.pattern(2111513)
    [<Pattern id='2111513' title='Converse on Nothing'>]


Lovers
------

The ColourLovers.com API provides two different ways to retrieve a
'lover' or a list of 'lovers'.

1. Searching for a single lover by calling the ``ColourLovers.lover()``
   method with the desired lover's user name, e.g. ``Alkalaiblue``. This will
   return the corresponding lover as ``ColourLovers.Lover`` instance.
2. Searching  for multiple lovers by calling ``ColourLovers.lovers()``
   with one of these arguments: ``new`` and  ``top`` (``random`` is not
   available in this case). This will return a list of
   ``ColourLovers.Lover`` objects.

For details on additional parameters please refer to the documentation at
http://python-colourlovers.readthedocs.org


Example::

    >>> from colourlovers import ColourLovers
    >>> cl = ColourLovers()
    >>> cl.lovers('new', numResults=4)
    [<Lover username='alliesuesue'>,
     <Lover username='NAJ910'>,
     <Lover username='VooDooDoll23'>,
     <Lover username='kidknie'>]
    >>> cl.lover('Alkalaiblue')
    [<Lover username='Alkalaiblue'>]

Stats
-----

To retrieve some basic statistics for certain content types provided on
ColourLovers.com you can call ``ColourLovers.stats`` with one of the following
*stat_types*: ``colours``, ``palettes``, ``patterns``, ``lovers``. Each call
returns a ``ColourLovers.Stats`` instance holding the total number of the
requested content type on ColourLovers.com.

Example::

    >>> from colourlovers import ColourLovers
    >>> cl = ColourLovers()
    >>> cl.stats('lovers')
    <Stat total='1113083'>
    >>> cl.stats('patterns')
    <Stat total='2096087'>
