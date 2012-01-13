#! /usr/bin/env python
# -*- coding: utf-8 -*-

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

    __CAPITAL_SPLIT = re.compile(r'[A-Z][^A-Z]+')
    __TYPE_MAP = {
        'id': 'int',
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
        'colorWidth': 'float',
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
        raise NotImplementedError()

    @classmethod
    def from_xml(cls, xml):
        kwargs = {}
        for child in xml.getchildren():
            if len(child.getchildren()) == 0:
                attr_name = cls.name_from_tag(child.tag)
                kwargs[attr_name] = child.text

        return cls(**kwargs)

    @classmethod
    def name_from_tag(cls, tag):
        tag = tag[0].upper() + tag[1:]
        result = cls.__CAPITAL_SPLIT.findall(tag)

        return '_'.join([x.lower() for x in result])

    @staticmethod
    def convert_date(value):
        return datetime.strptime(value, DATE_FORMAT)

    @staticmethod
    def convert_int(value):
        return int(value.replace(',', ''))

    @staticmethod
    def convert_float(value):
        return float(value)


class RGB(object):
    
    def __init__(self, red, green, blue):
        self.red = int(red)
        self.green = int(green)
        self.blue = int(blue)

    @property
    def hex(self):
        return '#%02x%02x%02x' % (self.red, self.green, self.blue) 

    @classmethod
    def from_xml(cls, xml):
        red = xml.find('red').text
        green = xml.find('green').text
        blue = xml.find('blue').text

        return cls(red, green, blue)

    def __repr__(self):
        return "<%s (%s, %s, %s)>" % (
            self.__class__.__name__,
            self.red,
            self.green,
            self.blue
        )

class HSV(object):
    
    def __init__(self, hue, saturation, value):
        self.hue = int(hue)
        self.saturation = int(saturation)
        self.value = int(value)

    @classmethod
    def from_xml(cls, xml):
        hue = xml.find('hue').text
        saturation = xml.find('saturation').text
        value = xml.find('value').text

        return cls(hue, saturation, value)

    def __repr__(self):
        return "<%s (%s, %s, %s)>" % (
            self.__class__.__name__,
            self.hue,
            self.saturation,
            self.value
        )

class Comment(object):

    def __init__(self, date, username, comments):
        self.comment_date = date
        self.comment_user_name = username
        self.comment_comments = comments 

    @classmethod
    def from_xml(cls, xml):
        return cls(
            datetime.strptime(
                xml.find('commentDate').text,
                DATE_FORMAT
            ),
            xml.find('commentUserName').text, 
            xml.find('commentComments').text
        )

class Colour(Base):

    def __init__(self, **kwargs):
        super(Colour, self).__init__(**kwargs)

        self.rgb = None
        self.hsv = None

    @classmethod
    def tag(cls):
        return 'color'

    @classmethod
    def from_xml(cls, xml):
        inst = super(Colour, cls).from_xml(xml)

        inst.hsv = HSV.from_xml(xml.find('hsv'))
        inst.rgb = RGB.from_xml(xml.find('rgb'))

        return inst

    def __repr__(self):
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
        return u"<%s id='%d' username='%s'>" % (
            self.__class__.__name__,
            self.id,
            self.userName.encode('ascii', 'ignore')
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

    def __init__(self):
        pass

    def stats(self, stat_type):
        if stat_type not in ['colors', 'lovers', 'patterns', 'palettes']:
            raise ColourLoversError("cannot retrieve stats for '%s'", stat_type)

        xml = self.__call('stats', stat_type)

        return Stat.from_xml(xml)

    def __getattr__(self, method):
        def proxy(argument=None, method=method, **kwargs):
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
            argument = argument.replace("#", '')
            url = "%s/%s/%s" % (self.API_URL, method, argument)

        ## no parameters can be set for 'random'
        if argument == 'random':
            kwargs = {}

        request = urllib2.Request(
            url, 
            data=urllib.urlencode(kwargs),
            headers={'User-Agent': "ColourLovers Browser"}
        )

        return self.__check_response(urllib2.urlopen(request).read())

        
    def __check_response(self, response):
        try:
            xml = ElementTree.XML(response)
        except:
            raise ColourLoversError(
                "could not retrieve result for your request"
            )
        return xml


