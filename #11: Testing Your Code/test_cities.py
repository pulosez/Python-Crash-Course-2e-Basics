import unittest
from city_functions import get_city_info


class CitiesTestCase(unittest.TestCase):

    def test_city_country_info(self):
        city_info = get_city_info('santiago', 'chile')
        self.assertEqual(city_info, 'Santiago, Chile')

    def test_city_country_population_info(self):
        city_info = get_city_info('santiago', 'chile', 5_000_000)
        self.assertEqual(city_info, 'Santiago, Chile - population 5000000')


if __name__ == '__main__':
    unittest.main()
