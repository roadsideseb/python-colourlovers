import httpretty

from colourlovers import ColourLovers, Colour, ColourLoversError

from tests.testcases import FixtureTestCase


class TestQueryingApi(FixtureTestCase):
    API_URL = 'http://www.colourlovers.com/api'
    fixtures = ['tests/fixtures/colour.xml']

    def test_for_colour_returns_valid_object(self):
        httpretty.enable()
        httpretty.register_uri(
            httpretty.GET,
            "{0}/color".format(self.API_URL),
            body=self.data['colour.xml']
        )

        cl = ColourLovers()
        colours = cl.color('#37cbff')

        self.assertTrue(isinstance(colours[0], Colour))
        self.assertEquals(colours[0].hex, '#37cbff')

        httpretty.disable()
