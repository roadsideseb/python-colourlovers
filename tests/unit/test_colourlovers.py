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

import mock
import unittest

from datetime import datetime

import colourlovers as cl

from tests.testcases import FixtureTestCase

try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree


class TestARgbValue(unittest.TestCase):

    def test_can_be_created_from_xml(self):
        xml = "<rgb><red>107</red><green>65</green><blue>6</blue></rgb>"

        rgb = cl.RGB.from_xml(ElementTree.XML(xml))

        self.assertEquals(rgb.red, 107)
        self.assertEquals(rgb.green, 65)
        self.assertEquals(rgb.blue, 6)
        self.assertEquals(rgb.hex, '#6b4106')


class TestAHsvValue(unittest.TestCase):

    def test_can_be_created_from_xml(self):
        xml = "<hsv><hue>35</hue>" +\
              "<saturation>94</saturation><value>42</value></hsv>"

        hsv = cl.HSV.from_xml(ElementTree.XML(xml))

        self.assertEquals(hsv.hue, 35)
        self.assertEquals(hsv.saturation, 94)
        self.assertEquals(hsv.value, 42)


class TestBase(FixtureTestCase):
    fixtures = ['tests/fixtures/palette.xml']

    def test_can_be_created_from_xml(self):
        xml = ElementTree.XML(self.data['palette.xml'])
        base = cl.Base.from_xml(xml)
        #TODO missing assertions

    def test_pythonic_name_can_be_created_from_camel_case(self):
        name = cl.Base.name_from_tag('userNameTest')
        self.assertEquals(name, 'user_name_test')

        name = cl.Base.name_from_tag('dateCreated')
        self.assertEquals(name, 'date_created')

        name = cl.Base.name_from_tag('id')
        self.assertEquals(name, 'id')


class TestAColour(FixtureTestCase):
    fixtures = ['tests/fixtures/colour.xml']

    def test_can_be_created_from_xml(self):
        xml = ElementTree.XML(self.data['colour.xml'])

        colour = cl.Colour.from_xml(xml)
        self.assertEquals(colour.id, 903893)
        self.assertEquals(colour.title, u'wet dirt')
        self.assertEquals(colour.user_name, u'jessicabrown')
        self.assertEquals(colour.num_views, 0)
        self.assertEquals(colour.num_votes, 0)
        self.assertEquals(colour.num_comments, 0)
        self.assertEquals(colour.num_hearts, 0)
        self.assertEquals(colour.rank, 903853)
        self.assertEquals(
            colour.date_created,
            datetime(2008, 3, 17, 11, 22, 21)
        )
        self.assertEquals(colour.hex, '#6b4106')

        self.assertEquals(colour.rgb.red, 107)
        self.assertEquals(colour.rgb.green, 65)
        self.assertEquals(colour.rgb.blue, 6)

        self.assertEquals(colour.hsv.hue, 35)
        self.assertEquals(colour.hsv.saturation, 94)
        self.assertEquals(colour.hsv.value, 42)

        self.assertEquals(colour.description, None)
        self.assertEquals(
            colour.url,
            'http://www.colourlovers.com/color/6B4106/wet_dirt'
        )
        self.assertEquals(
            colour.image_url,
            u'http://www.colourlovers.com/img/6B4106/100/100/wet_dirt.png'
        )
        self.assertEquals(
            colour.badge_url,
            u'http://www.colourlovers.com/images/badges/c/903/903893_wet_dirt.png'
        )
        self.assertEquals(
            colour.api_url,
            u'http://www.colourlovers.com/api/color/6B4106'
        )


class TestPalette(FixtureTestCase):
    fixtures = ['tests/fixtures/palette.xml']

    def test_can_be_created_from_xml(self):
        xml = ElementTree.XML(self.data['palette.xml'])

        palette = cl.Palette.from_xml(xml)

        self.assertEquals(palette.id, 12345)
        self.assertEquals(palette.title, 'be my boy')
        self.assertEquals(palette.user_name, 'sinta schneider')
        self.assertEquals(palette.num_views, 1052)
        self.assertEquals(palette.num_votes, 37)
        self.assertEquals(palette.num_comments, 13)
        self.assertEquals(palette.num_hearts, 4.5)
        self.assertEquals(palette.rank, 1)
        self.assertEquals(palette.date_created, datetime(2008, 3, 1, 16, 19, 21))

        self.assertEquals(len(palette.colours), 5)
        self.assertEquals(palette.colours, [
            '#423238',
            '#f5de8c',
            '#c8d197',
            '#b3702d',
            '#eb2138'
        ])

        self.assertEquals(palette.color_widths, [0.2, 0.2, 0.2, 0.2, 0.2])

        self.assertEquals(palette.description, None)
        self.assertEquals(
            palette.url,
            'http://www.colourlovers.com/palette/293826/be_my_boy'
        )
        self.assertEquals(
            palette.image_url,
            'http://www.colourlovers.com/paletteImg/423238/F5DE8C/C8D197/B3702D/EB2138/be_my_boy.png'
        )
        self.assertEquals(
            palette.badge_url,
            'http://www.colourlovers.com/images/badges/p/293/293826_be_my_boy.png'
        )
        self.assertEquals(
            palette.api_url,
            'http://www.colourlovers.com/api/palette/293826'
        )


class TestPattern(FixtureTestCase):
    fixtures = ['tests/fixtures/pattern.xml']

    def test_can_be_created_from_xml(self):
        xml = ElementTree.XML(self.data['pattern.xml'])

        pattern = cl.Pattern.from_xml(xml)

        self.assertEquals(pattern.id, 12345)
        self.assertEquals(pattern.title, 'Tenderness.')
        self.assertEquals(pattern.user_name, 'not.an.am.person')
        self.assertEquals(pattern.num_views, 617)
        self.assertEquals(pattern.num_votes, 32)
        self.assertEquals(pattern.num_comments, 14)
        self.assertEquals(pattern.num_hearts, 4.5)
        self.assertEquals(pattern.rank, 1)
        self.assertEquals(
            pattern.date_created,
            datetime(2008, 3, 1, 6, 43, 38)
        )

        self.assertEquals(len(pattern.colours), 5)
        self.assertEquals(pattern.colours, [
            '#c6c5ac',
            '#cdb89f',
            '#d4aa93',
            '#b8e0c5',
            '#bfd3b8'
        ])
        self.assertEquals(pattern.description, None)
        self.assertEquals(
            pattern.url,
            'http://www.colourlovers.com/pattern/49471/Tenderness.'
        )
        self.assertEquals(
            pattern.image_url,
            'http://colourlovers.com.s3.amazonaws.com/images/patterns/49/49471.png'
        )
        self.assertEquals(
            pattern.badge_url,
            'http://www.colourlovers.com/images/badges/n/49/49471_Tenderness..png'
        )
        self.assertEquals(
            pattern.api_url,
            'http://www.colourlovers.com/api/pattern/49471'
        )


class TestLover(FixtureTestCase):
    fixtures = ['tests/fixtures/lover.xml']

    def test_can_be_created_from_xml(self):
        xml = ElementTree.XML(self.data['lover.xml'])

        lover = cl.Lover.from_xml(xml)

        self.assertEquals(lover.user_name, u'electrikmönk')
        self.assertEquals(
            lover.date_registered,
            datetime(2005, 8, 7, 6, 45, 47)
        )
        self.assertEquals(
            lover.date_last_active,
            datetime(2008, 3, 16, 21, 2, 1)
        )
        self.assertEquals(lover.rating, 554159)
        self.assertEquals(lover.location, u'#FF0000stick, LA, US')
        self.assertEquals(lover.num_colors, 3498)
        self.assertEquals(lover.num_palettes, 2775)
        self.assertEquals(lover.num_patterns, 36)
        self.assertEquals(lover.num_comments_made, 7201)
        self.assertEquals(lover.num_lovers, 710)
        self.assertEquals(lover.num_comments_on_profile, 672)

        self.assertEquals(len(lover.comments), 1)
        comment = lover.comments[0]
        self.assertEquals(
            comment.comment_date,
            datetime(2008, 3, 10, 5, 10, 58)
        )
        self.assertEquals(comment.comment_user_name, u'mashedpotato')
        self.assertEquals(comment.comment_comments, u'you are so awesome. :x ')

        self.assertEquals(
            lover.url,
            u'http://www.colourlovers.com/lover/electrikmonk'
        )
        self.assertEquals(
            lover.api_url,
            u'http://www.colourlovers.com/api/lover/electrikmonk'
        )


class TestStat(unittest.TestCase):

    def test_can_be_created_from_xml(self):
        xml = ElementTree.XML('<stats><total>1500563</total></stats>')
        stat = cl.Stat.from_xml(xml)

        self.assertEquals(stat.total, 1500563)


class TestColourLoversApi(unittest.TestCase):

    def test_can_retrieve_color_from_hex_value(self):
        cl_api = cl.ColourLovers()

        for hexstr in ['6B4106', '#6b4106']:
            res = cl_api.color(hexstr)
            self.assertEquals(len(res), 1)
            self.assertEquals(type(res[0]), cl.Colour)
            self.assertEquals(res[0].hex, '#6b4106')

    def test_retrieving_color_from_invalid_hex_raises_an_exception(self):
        cl_api = cl.ColourLovers()

        self.assertRaises(cl.ColourLoversError, cl_api.color, '6B410')

    def test_provides_valid_list_of_methods(self):
        self.assertEquals(
            cl.ColourLovers.valid_methods(),
            ['color', 'palette', 'pattern', 'lover',
             'colors', 'palettes', 'patterns', 'lovers', 'stats']
        )

    def test_can_convert_keywords_from_dashed_to_camelcase(self):
        keywords = {
            "order_col": 'score',
            "sortBy": 'DESC',
            "num_results": 20,
            "result_offset": 5,
            "format": 'json',
            "jsonCallback": 'somecallbackfunction',
        }
        converted_keywords = cl.ColourLovers().convert_keywords(keywords)

        self.assertEquals(len(converted_keywords), 4)
        self.assertItemsEqual(
            converted_keywords.keys(),
            ['orderCol', 'sortBy', 'numResults', 'resultOffset']
        )

    def test_can_retrieve_colours_for_special_keywords(self):
        cl_api = cl.ColourLovers()

        for argument in ['new', 'top', 'random']:
            results = cl_api.colors(argument)

            for result in results:
                self.assertEquals(type(result), cl.Colour)

    def test_retrieving_colours_with_invalid_keyword_raises_exception(self):
        cl_api = cl.ColourLovers()

        self.assertRaises(
            cl.ColourLoversError,
            cl_api.colors,
            'invalid_argument'
        )

    def test_checking_error_response_raises_an_exception(self):
        response = mock.MagicMock()
        response.status_code = 404

        cl_api = cl.ColourLovers()
        self.assertRaises(
            cl.ColourLoversError,
            cl_api._check_response,
            response
        )
