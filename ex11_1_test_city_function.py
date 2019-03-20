import unittest
from ex11_1_city_function import city_function


class CityTestCase(unittest.TestCase):
    def test_city_function(self):
        formatted_name = city_function('huizhou', 'china')
        self.assertEqual(formatted_name, 'Huizhou, China')

    def test_population_function(self):
        formatted_name = city_function('huizhou', 'china', 4000000)
        self.assertEqual(formatted_name, 'Huizhou, China - 4000000')


unittest.main
