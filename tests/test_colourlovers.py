# -*- coding: utf-8 -*-

import unittest
from datetime import datetime

try:
    from xml.etree import ElementTree
except ImportError:
    from elementtree import ElementTree

from colourlovers import ColourLoversError

from colourlovers import RGB

class TestRGB(unittest.TestCase):

    def test_from_xml(self):
        xml = "<rgb><red>107</red><green>65</green><blue>6</blue></rgb>"

        rgb = RGB.from_xml(ElementTree.XML(xml)) 

        self.assertEquals(rgb.red, 107)
        self.assertEquals(rgb.green, 65)
        self.assertEquals(rgb.blue, 6)
        self.assertEquals(rgb.hex, '#6b4106')

from colourlovers import HSV 

class TestHSV(unittest.TestCase):

    def test_from_xml(self):
        xml = "<hsv><hue>35</hue>" +\
              "<saturation>94</saturation><value>42</value></hsv>"

        hsv = HSV.from_xml(ElementTree.XML(xml)) 

        self.assertEquals(hsv.hue, 35)
        self.assertEquals(hsv.saturation, 94)
        self.assertEquals(hsv.value, 42)


from colourlovers import Base

class TestBase(unittest.TestCase):

    def test_from_xml(self):
        xml = ElementTree.XML(PALETTE_XML)

        base = Base.from_xml(xml)

    def test_name_from_tag(self):
        name = Base.name_from_tag('userNameTest')
        self.assertEquals(name, 'user_name_test')

        name = Base.name_from_tag('dateCreated')
        self.assertEquals(name, 'date_created')

        name = Base.name_from_tag('id')
        self.assertEquals(name, 'id')

from colourlovers import Colour 

class TestColour(unittest.TestCase):

    def test_from_xml(self):
        xml = ElementTree.XML(COLOUR_XML)

        colour = Colour.from_xml(xml)
        self.assertEquals(colour.id, 903893)
        self.assertEquals(colour.title, u'wet dirt')
        self.assertEquals(colour.user_name, u'jessicabrown')
        self.assertEquals(colour.num_views, 0)
        self.assertEquals(colour.num_votes, 0)
        self.assertEquals(colour.num_comments, 0)
        self.assertEquals(colour.num_hearts, 0)
        self.assertEquals(colour.rank, 903853)
        self.assertEquals(colour.date_created, datetime(2008, 3, 17, 11, 22, 21))
        self.assertEquals(colour.hex, '#6b4106')
        
        self.assertEquals(colour.rgb.red, 107)
        self.assertEquals(colour.rgb.green, 65)
        self.assertEquals(colour.rgb.blue, 6)

        self.assertEquals(colour.hsv.hue, 35)
        self.assertEquals(colour.hsv.saturation, 94)
        self.assertEquals(colour.hsv.value, 42)

        self.assertEquals(colour.description, None) 
        self.assertEquals(colour.url, 'http://www.colourlovers.com/color/6B4106/wet_dirt')
        self.assertEquals(colour.image_url, u'http://www.colourlovers.com/img/6B4106/100/100/wet_dirt.png')
        self.assertEquals(colour.badge_url, u'http://www.colourlovers.com/images/badges/c/903/903893_wet_dirt.png')
        self.assertEquals(colour.api_url, u'http://www.colourlovers.com/api/color/6B4106')


from colourlovers import Palette 

class TestPalette(unittest.TestCase):

    def test_from_xml(self):
        xml = ElementTree.XML(PALETTE_XML)

        palette = Palette.from_xml(xml)


from colourlovers import Pattern

class TestPattern(unittest.TestCase):

    def test_from_xml(self):
        xml = ElementTree.XML(PATTERN_XML)

        parttern = Pattern.from_xml(xml)


from colourlovers import Lover 

class TestLover(unittest.TestCase):

    def test_from_xml(self):
        xml = ElementTree.XML(LOVER_XML)

        lover = Lover.from_xml(xml)

        self.assertEquals(lover.user_name, u'electrikmönk')
        self.assertEquals(lover.date_registered, datetime(2005, 8, 7, 6, 45, 47))
        self.assertEquals(lover.date_last_active, datetime(2008, 3, 16, 21, 2, 1))
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
        self.assertEquals(comment.comment_date, datetime(2008, 3, 10, 5, 10, 58))
        self.assertEquals(comment.comment_user_name, u'mashedpotato')
        self.assertEquals(comment.comment_comments, u'you are so awesome. :x ')

        self.assertEquals(lover.url, u'http://www.colourlovers.com/lover/electrikmonk')
        self.assertEquals(lover.api_url, u'http://www.colourlovers.com/api/lover/electrikmonk')

from colourlovers import Stat 

class TestStat(unittest.TestCase):

    def test_from_xml(self):
        xml = ElementTree.XML('<stats><total>1500563</total></stats>')
        stat = Stat.from_xml(xml)

        self.assertEquals(stat.total, 1500563)


from colourlovers import ColourLovers

class TestColourLovers(unittest.TestCase):

    def test_method_calls(self):
        cl_api = ColourLovers()
        res = cl_api.color('6B4106')
        res = cl_api.color('#6B4106')

        self.assertRaises(
            ColourLoversError,
            cl_api.color,
            '6B410'
        )

COLOUR_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<color>
  <id>903893</id>
  <title><![CDATA[wet dirt]]></title>
  <userName><![CDATA[jessicabrown]]></userName>
  <numViews>0</numViews>
  <numVotes>0</numVotes>
  <numComments>0</numComments>
  <numHearts>0</numHearts>
  <rank>903853</rank>
  <dateCreated>2008-03-17 11:22:21</dateCreated>
  <hex>6B4106</hex>
  <rgb>
     <red>107</red>
     <green>65</green>
     <blue>6</blue>
  </rgb>
  <hsv>
     <hue>35</hue>
     <saturation>94</saturation>
     <value>42</value>
  </hsv>
  <description><![CDATA[]]></description>
  <url><![CDATA[http://www.colourlovers.com/color/6B4106/wet_dirt]]></url>
  <imageUrl><![CDATA[http://www.colourlovers.com/img/6B4106/100/100/wet_dirt.png]]></imageUrl>
  <badgeUrl><![CDATA[http://www.colourlovers.com/images/badges/c/903/903893_wet_dirt.png]]></badgeUrl>
  <apiUrl>http://www.colourlovers.com/api/color/6B4106</apiUrl>
</color>"""

PALETTE_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<palette>
    <id>12345</id>
    <title><![CDATA[be my boy]]></title>
    <userName><![CDATA[sinta schneider]]></userName>
    <numViews>1052</numViews>
    <numVotes>37</numVotes>
    <numComments>13</numComments>
    <numHearts>4.5</numHearts>
    <rank>1</rank>
    <dateCreated>2008-03-01 16:19:21</dateCreated>
    <colors>
      <hex>423238</hex>
      <hex>F5DE8C</hex>
      <hex>C8D197</hex>
      <hex>B3702D</hex>
      <hex>EB2138</hex>
    </colors>
    <!-- Optional color widths [Only returned with the ?showPaletteWidths=1] -->
    <colorWidths>0.2,0.2,0.2,0.2,0.2</colorWidths>
    <description><![CDATA[]]></description>
    <url><![CDATA[http://www.colourlovers.com/palette/293826/be_my_boy]]></url>
    <imageUrl><![CDATA[http://www.colourlovers.com/paletteImg/423238/F5DE8C/C8D197/B3702D/EB2138/be_my_boy.png]]></imageUrl>
    <badgeUrl><![CDATA[http://www.colourlovers.com/images/badges/p/293/293826_be_my_boy.png]]></badgeUrl>
    <apiUrl>http://www.colourlovers.com/api/palette/293826</apiUrl>
  </palette>"""

PATTERN_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<pattern>
    <id>12345</id>
    <title><![CDATA[Tenderness.]]></title>
    <userName><![CDATA[not.an.am.person]]></userName>
    <numViews>617</numViews>
    <numVotes>32</numVotes>
    <numComments>14</numComments>
    <numHearts>4.5</numHearts>
    <rank>1</rank>
    <dateCreated>2008-03-01 06:43:38</dateCreated>
    <colors>
      <hex>C6C5AC</hex>
      <hex>CDB89F</hex>
      <hex>D4AA93</hex>
      <hex>B8E0C5</hex>
      <hex>BFD3B8</hex>
    </colors>
    <description><![CDATA[]]></description>
    <url><![CDATA[http://www.colourlovers.com/pattern/49471/Tenderness.]]></url>
    <imageUrl><![CDATA[http://colourlovers.com.s3.amazonaws.com/images/patterns/49/49471.png]]></imageUrl>
    <badgeUrl><![CDATA[http://www.colourlovers.com/images/badges/n/49/49471_Tenderness..png]]></badgeUrl>
    <apiUrl>http://www.colourlovers.com/api/pattern/49471</apiUrl>
  </pattern>"""

LOVER_XML = """<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<lover>
    <id>12345</id>
    <userName><![CDATA[electrikmönk]]></userName>
    <dateRegistered>2005-08-07 6:45:47</dateRegistered>
    <dateLastActive>2008-03-16 21:02:01</dateLastActive>
    <rating>554159</rating>
    <location><![CDATA[#FF0000stick, LA, US]]></location>
    <numColors>3,498</numColors>
    <numPalettes>2,775</numPalettes>
    <numPatterns>36</numPatterns>
    <numCommentsMade>7,201</numCommentsMade>
    <numLovers>710</numLovers>
    <numCommentsOnProfile>672</numCommentsOnProfile>
    <!-- Optional comments [Only returned when viewing one Lover with the ?comments=1] -->
    <comments>
      <comment>
        <commentDate>2008-03-10 05:10:58</commentDate>
        <commentUserName><![CDATA[mashedpotato]]></commentUserName>
        <commentComments><![CDATA[you are so awesome. :x ]]></commentComments>
      </comment>
    </comments>
    <url><![CDATA[http://www.colourlovers.com/lover/electrikmonk]]></url>
    <apiUrl><![CDATA[http://www.colourlovers.com/api/lover/electrikmonk]]></apiUrl>
  </lover>"""
