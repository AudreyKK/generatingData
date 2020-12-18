import unittest
from country_codes import get_country_code

class CountryCodesTestCase(unittest.TestCase):
    """Tests for country_code.py"""

    def test_cc(self):
        """Do the correct country codes get returned?"""
        cc = get_country_code('Japan')
        self.assertEqual(cc, 'jp')

    def test_missing_cc(self):
        """Respond to country codes that are not found in pygal/COUNTRIES"""
        cc = get_country_code('Bolivia')
        self.assertEqual(cc, 'bol')

unittest.main()
