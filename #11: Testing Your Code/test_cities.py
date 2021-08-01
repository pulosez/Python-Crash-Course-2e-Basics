import unittest
from city_functions import get_city_info


class CitiesTestCase(unittest.TestCase):

    def test_city_country_info(self):
        city_info = get_city_info('santiago', 'chile')
        self.assertEqual(city_info, 'Santiago, Chile')


if __name__ == '__main__':
    unittest.main()
