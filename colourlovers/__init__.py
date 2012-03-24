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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
This module provides access to the ColourLovers API, a web service
that allows users to publish colour themes and rate them. The API of
this webservice allows to search for users (Lovers) and their posted
contents (Colours, Patterns, Palettes).

Accessing the API requires an instance of :py:class:`ColourLovers`
which provides the methods to access the different content types:
*Colour*, *Palette*, *Pattern*, *Lover*. Sending a request to
ColourLovers is as easy as calling the corresponding method such as
:py:meth:`ColourLovers.palettes` to search for palettes.
Additionally, the following arguments can be specified ``new``, ``top``,
``random`` with additional parameters. Please refer to the ColourLovers
API documentation to find out more about the specific parameters and
their restrictions at http://www.colourlovers.com/api.

You find the ColourLovers website at: http://www.colourlovers.com

Usage example::

    >>> from colourlovers import ColourLovers
    >>> cl = ColourLovers()
    >>> cl.color('#37cbff')
    [<Colour id='4767129' title='i feel pretty' rgb=(55, 203, 255)>]
    >>> cl.palettes('new', keywords='funky', numResults=3)
    [<Palette id='1940972' title='"Funky President"'>,
     <Palette id='1936394' title='Barbie Doll Blonde'>,
     <Palette id='1936247' title='Lily's Rainbow'>]

Another example::

    >>> cl.patterns('random')
    [<Pattern id='391644' title='acanalado'>]
    >>> cl.colors('top', numResults=3)
    [<Colour id='14' title='Black' rgb=(0, 0, 0)>,
     <Colour id='16' title='white' rgb=(255, 255, 255)>,
     <Colour id='1086335' title='dutch teal' rgb=(22, 147, 165)>]
"""

import re
import urllib
import urllib2

from datetime import datetime

try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree


DATE_FORMAT = '%Y-%m-%d %H:%M:%S'


class ColourLoversError(BaseException):
    pass

class Base(object):
    """ Define the base class for content types as provided
        by the ColourLovers API.
    """

    __CAPITAL_SPLIT = re.compile(r'[A-Z][^A-Z]+')
    __TYPE_MAP = {
        'id': 'int',
        'hex': 'hex',
        'rank': 'int',
        'rating': 'int',
        'num_views': 'int',
        'num_votes': 'int',
        'num_lovers': 'int',
        'num_colors': 'int',
        'num_hearts': 'float',
        'num_palettes': 'int',
        'num_patterns': 'int',
        'num_comments': 'int',
        'num_comments_made': 'int',
        'num_comments_on_profile': 'int',
        'color_widths': 'float_list',
        'date_created': 'date',
        'date_registered': 'date',
        'date_last_active': 'date',
    }

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key in self.__TYPE_MAP:
                datatype = self.__TYPE_MAP[key]
                value = getattr(self, 'convert_%s' % datatype)(value)

            setattr(self, key, value)

    @classmethod
    def tag(cls):
        """ Abstract method to be overwritten in subclasses. Should
            return the tag used in the XML response to identify the
            corresponding content type.
        """
        raise NotImplementedError()

    @classmethod
    def from_xml(cls, xml):
        """ Parse *xml* and generate class attributes for each immediate
            child of the root element without children of their own.

            Args:
                *xml (``Element``)*: xml element of content type.

            Returns:
                Instance of calling class.
        """
        kwargs = {}
        for child in xml.getchildren():
            if len(child.getchildren()) == 0:
                attr_name = cls.name_from_tag(child.tag)
                kwargs[attr_name] = child.text

        return cls(**kwargs)

    @classmethod
    def name_from_tag(cls, tag):
        """ Generate a Pythonic attribute name from the
            CamelCase tag names provided in the ColourLovers XML
            response.

            Args:
                *tag (str)*: XML tag name in CamelCase.

            Returns:
                Pythonic attribute name as ``str``.
        """
        tag = tag[0].upper() + tag[1:]
        result = cls.__CAPITAL_SPLIT.findall(tag)

        return '_'.join([x.lower() for x in result])

    @staticmethod
    def convert_date(value):
        """ Convert date in *value* to corresponding
            ``datetime.datetime`` format.

            Args:
                *value (str)*: date & time representation.

            Returns:
                ``datetime.datetime`` object according to format.
        """
        return datetime.strptime(value, DATE_FORMAT)

    @staticmethod
    def convert_int(value):
        """ Convert *value* to ``int``. *value* might contain ',' to
            separate the thousand, million, etc. digits block.

            Args:
                *value (str)*: integer value to convert.

            Returns:
                ``int`` of value.
        """
        return int(value.replace(',', ''))

    @staticmethod
    def convert_float(value):
        """ Convert *value* to ``float``.

            Args:
                *value (str)*: float value to convert.

            Returns:
                ``float`` of value.
        """
        return float(value)

    @staticmethod
    def convert_hex(value):
        """ Convert hex colour code in *value* as received from
            API response to '#xxxxxx' format. Letters in hex format
            are lowercase.

            Args:
                *value (str)*: value containing hex colour code.

            Returns:
                Cleaned up hex colour code as ``str``.
        """
        return '#' + value.lower()

    @staticmethod
    def convert_float_list(value):
        """ Convert a list of floats in *value* to a Python list.

            Args:
                *value (str)*: value containing list of floats.

            Returns:
                Float values as ``list``.
        """
        return [float(x.strip()) for x in value.split(',')]

class RGB(object):
    """ Define a RGB colour as a triple of integers in the
        range from 0 to 255. The colour channels are stored in
        attributes :py:attr:`red`, :py:attr:`green`, :py:attr:`blue`.
    """

    def __init__(self, red, green, blue):
        """ Construct an instance of :py:class:`RGB` from *red*, *green*
            and *blue*. The three colour values have to be whole numbers
            in the range [0, 255].

            Args:
                *red (int, str)*: integer value for the red channel.
                *green (int, str)*: integer value for the green channel.
                *blue (int, str)*: integer value for the blue channel.
        """
        self.red = int(red)
        self.green = int(green)
        self.blue = int(blue)

    @property
    def hex(self):
        """ Return hex colour code corresponding to the RGB value. """
        return '#%02x%02x%02x' % (self.red, self.green, self.blue)

    @classmethod
    def from_xml(cls, xml):
        """ Create an instance of :py:class:`RGB` from *xml*.

            Args:
                *xml (Element)*: ``rgb`` element from API response.

            Returns:
                Instance of :py:class:`RGB`.
        """
        red = xml.find('red').text
        green = xml.find('green').text
        blue = xml.find('blue').text

        return cls(red, green, blue)

    def __repr__(self):
        """ Return representation of RGB instance. """
        return "<%s (%s, %s, %s)>" % (
            self.__class__.__name__,
            self.red,
            self.green,
            self.blue
        )


class HSV(object):
    """ Define a HSV colour instance from *hue*, *saturation* and *value*.
        The three values have to be integer values with *hue* in range [0, 360]
        and *saturation*, *value* in range [0, 255].
    """

    def __init__(self, hue, saturation, value):
        """ Construct a HSV colour instance from *hue*, *saturation*, *value*.
            All three values have to be whole numbers. *hue* has to be in range
            [0, 360], *saturation* and *value* have to be in range [0, 255].

            Args:
                *hue (int, str)*: HSV hue channel value.
                *saturation (int, str)*: HSV saturation channel value.
                *value (int, str)*: HSV value channel value.
        """
        self.hue = int(hue)
        self.saturation = int(saturation)
        self.value = int(value)

    @classmethod
    def from_xml(cls, xml):
        """ Create an instance of :py:class:`HSV` from *xml*.

            Args:
                *xml (Element)*: ``hsv`` element from API response.

            Returns:
                Instance of :py:class:`HSV`.
        """
        hue = xml.find('hue').text
        saturation = xml.find('saturation').text
        value = xml.find('value').text

        return cls(hue, saturation, value)

    def __repr__(self):
        """ Return string representation of HSV instance. """
        return "<%s (%s, %s, %s)>" % (
            self.__class__.__name__,
            self.hue,
            self.saturation,
            self.value
        )

class Comment(object):
    """ The comment class represents a comment for a ColourLovers
        user as returned by the *lovers* API request. The comment
        provides the *date*, *username* and *comments* text.
    """

    def __init__(self, date, username, comments):
        """ Create a comment created at *date* from user *username*
            with the comment text in *comments*. *date* has to be
            a datetime object.
        """
        self.comment_date = date
        self.comment_user_name = username
        self.comment_comments = comments

    @classmethod
    def from_xml(cls, xml):
        """ Create a comment object from *xml*. It expects a DOM
            element ``<comment>`` and extracts date, username and
            comment text from its sub-elements as describe in the
            ColourLovers API.

            Args:
                xml (Element): ``comment`` DOM element.

            Returns:
                New instance of class :py:class:`Comment`.
        """
        return cls(
            datetime.strptime(
                xml.find('commentDate').text,
                DATE_FORMAT
            ),
            xml.find('commentUserName').text,
            xml.find('commentComments').text
        )

class Colour(Base):
    """ This class defines a ColourLovers colour in the RGB and
        HSV colour spaces. The colour values can be accessed through
        the :py:attr:`rgb` and :py:attr:`hsv` respectively and are
        of type :py:class:`RGB` and :py:class:`HSV`.
    """

    def __init__(self, **kwargs):
        super(Colour, self).__init__(**kwargs)

        self.rgb = None
        self.hsv = None

    @classmethod
    def tag(cls):
        """ Returns the name of the XML tag for a colour object. """
        return 'color'

    @classmethod
    def from_xml(cls, xml):
        """ Create a new colour instance from *xml*. *xml* is a DOM
            element with the root element name ``color``.

            Args:
                xml (Element): ``color`` DOM element.

            Returns:
                New instance of :py:class:`Colour`.
        """
        inst = super(Colour, cls).from_xml(xml)

        inst.rgb = RGB.from_xml(xml.find('rgb'))
        inst.hsv = HSV.from_xml(xml.find('hsv'))

        return inst

    def __repr__(self):
        """ Return a representation of :py:class:`Colour` instance. """
        return "<%s id='%d' title='%s' rgb=(%d, %d, %d)>" % (
            self.__class__.__name__,
            self.id,
            self.title.encode('ascii', 'ignore'),
            self.rgb.red,
            self.rgb.green,
            self.rgb.blue
        )

class Palette(Base):

    def __init__(self, **kwargs):
        super(Palette, self).__init__(**kwargs)

        self.colours = []

    @classmethod
    def tag(cls):
        return 'palette'

    @classmethod
    def from_xml(cls, xml):
        inst = super(Palette, cls).from_xml(xml)

        for hex_colour in xml.findall('colors/hex'):
            inst.colours.append('#'+hex_colour.text.lower())

        return inst

    def __repr__(self):
        return u"<%s id='%d' title='%s'>" % (
            self.__class__.__name__,
            self.id,
            self.title.encode('ascii', 'ignore'),
        )

class Pattern(Base):

    def __init__(self, **kwargs):
        super(Pattern, self).__init__(**kwargs)

        self.colours = []

    @classmethod
    def tag(cls):
        return 'pattern'

    @classmethod
    def from_xml(cls, xml):
        inst = super(Pattern, cls).from_xml(xml)

        for hex_colour in xml.findall('colors/hex'):
            inst.colours.append('#'+hex_colour.text.lower())

        return inst

    def __repr__(self):
        return u"<%s id='%d' title='%s'>" % (
            self.__class__.__name__,
            self.id,
            self.title.encode('ascii', 'ignore'),
        )

class Lover(Base):

    def __init__(self, **kwargs):
        super(Lover, self).__init__(**kwargs)

        self.comments = []

    @classmethod
    def tag(cls):
        return 'lover'

    @classmethod
    def from_xml(cls, xml):
        inst = super(Lover, cls).from_xml(xml)

        for comment in xml.findall('comments/comment'):
            inst.comments.append(Comment.from_xml(comment))

        return inst

    def __repr__(self):
        return u"<%s username='%s'>" % (
            self.__class__.__name__,
            self.user_name.encode('ascii', 'ignore')
        )

class Stat(Base):

    def __init__(self, total, **kwargs):
        super(Stat, self).__init__(**kwargs)

        self.total = int(total)

    @classmethod
    def from_xml(cls, xml):
        return cls(xml.find('total').text)

    def __repr__(self):
        return u"<%s total='%d'>" % (
            self.__class__.__name__,
            self.total,
        )

class ColourLovers(object):

    API_URL = 'http://www.colourlovers.com/api'

    __CLASS_MAP = {
        'color': Colour,
        'colors': Colour,
        'palette': Palette,
        'palettes': Palette,
        'pattern': Pattern,
        'patterns': Pattern,
        'lover': Lover,
        'lovers': Lover,
        'stats': Stat,
    }

    __SPECIFIC_METHODS = ['color', 'palette', 'pattern', 'lover']
    __SEARCH_METHODS = ['colors', 'palettes', 'patterns', 'lovers']

    __ARGUMENTS = [None, 'new', 'top', 'random']

    def __init__(self):
        pass

    def stats(self, stat_type):
        """ Return the stats for *stat_type*. *stat_type* refers to one
            of the content types on ColourLovers and can be ``colors``,
            ``lovers``, ``patterns``, ``palettes``. A
            :py:exc:`ColourLoversError` is raised when an invalid type is
            requested.

            Args:
                *stat_type (str)*: content type to request stats for.

            Returns:
                The requested stats as :py:class:`Stat` object.
        """
        if stat_type not in ['colors', 'lovers', 'patterns', 'palettes']:
            raise ColourLoversError("cannot retrieve stats for '%s'", stat_type)

        xml = self.__call('stats', stat_type)

        return Stat.from_xml(xml)

    def __getattr__(self, method):
        if method not in self.__SPECIFIC_METHODS+self.__SEARCH_METHODS:
            raise ColourLoversError("invalid API method '%s'", method)

        def proxy(argument=None, method=method, **kwargs):
            if method in self.__SEARCH_METHODS \
                and argument not in self.__ARGUMENTS:
                    raise ColourLoversError(
                        "%s is invalid argument for '%s'" % (argument, method)
                    )
            xml = self.__call(method, argument, **kwargs)
            return self.__process(method, xml)

        return proxy

    def __process(self, method, xml):
        class_name = self.__CLASS_MAP[method]

        results = []
        for elem in xml.findall(class_name.tag()):
            results.append(
                class_name.from_xml(elem)
            )

        return results

    def __call(self, method, argument=None, **kwargs):
        if argument is None:
            url = "%s/%s" % (self.API_URL, method)
        else:
            ## make sure hex argument has no hash
            argument = str(argument).replace("#", '')
            url = "%s/%s/%s" % (self.API_URL, method, argument)

        ## no parameters can be set for 'random'
        if argument == 'random':
            kwargs = {}

        converted_kwargs = self.convert_keywords(kwargs)

        request = urllib2.Request(
            url,
            data=urllib.urlencode(converted_kwargs),
            headers={'User-Agent': "ColourLovers Browser"}
        )

        return self.__check_response(urllib2.urlopen(request).read())

    @classmethod
    def valid_methods(cls):
        return cls.__SPECIFIC_METHODS+cls.__SEARCH_METHODS+['stats']

    def convert_keywords(self, keywords):
        converted = {}
        for key, value in keywords.items():
            key_parts = key.split('_')

            new_key = key_parts[:1]
            for key_part in key_parts[1:]:
                new_key.append(key_part.capitalize())

            new_key = ''.join(new_key)

            if new_key not in ['format', 'jsonCallback']:
                converted[new_key] = value

        return converted

    @staticmethod
    def __check_response(response):
        """ Check the *response* for valid XML. An invalid request
            raises :py:class:ColourLoversError. An invalid request is determined
            by an empty response XML. ColourLovers does not provide
            additional error infomation.

            Keywords arguments:
            response -- string as returned by the ColourLovers API.
        """
        try:
            xml = ElementTree.XML(response)
        except:
            raise ColourLoversError(
                "could not retrieve result for your request"
            )
        return xml
