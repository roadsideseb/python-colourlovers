.. python-colourlovers documentation master file, created by
   sphinx-quickstart on Fri Jan 13 17:41:01 2012.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to python-colourlovers's documentation!
===============================================

.. automodule:: colourlovers

ColourLovers
------------

.. autoclass:: colourlovers.ColourLovers

    .. method:: color(argument, **kwargs)

    .. method:: colors(argument, **kwargs)

    .. method:: palette(argument, **kwargs)

    .. method:: palettes(argument, **kwargs)

    .. method:: pattern(argument, **kwargs)

    .. method:: patterns(argument, **kwargs)

    .. method:: lover(argument, **kwargs)

    .. method:: lovers(argument, **kwargs)

    .. automethod:: colourlovers.ColourLovers.stats

Colour
------

.. autoclass:: colourlovers.Colour
    :members:

Palette
-------

.. autoclass:: colourlovers.Palette
    :members:

Pattern
-------

.. autoclass:: colourlovers.Pattern
    :members:

Lover
-----

.. autoclass:: colourlovers.Lover
    :members:

Stat
----

.. autoclass:: colourlovers.Stat
    :members:

The RGB and HSV colour classes
------------------------------

.. autoclass:: colourlovers.RGB
    
    .. automethod:: colourlovers.RGB.from_xml

    .. attribute:: red

        Red colour channel in range [0, 255]       

    .. attribute:: green

        Green colour channel in range [0, 255]       

    .. attribute:: blue

        Blue colour channel in range [0, 255]       

    .. autoattribute:: colourlovers.RGB.hex

.. autoclass:: colourlovers.HSV
    
    .. automethod:: colourlovers.HSV.from_xml

    .. attribute:: hue 

        HSV hue channel in range [0, 360]       

    .. attribute:: saturation 

        HSV saturation channel in range [0, 255]       

    .. attribute:: value 

        HSV value channel in range [0, 255]       


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

