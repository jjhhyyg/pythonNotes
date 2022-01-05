import unittest

from city_function import city_country


class CityCountryTestCase(unittest.TestCase):
    def test_city_country(self):
        formatted_city_country = city_country("santiago", "chile")
        self.assertEqual(formatted_city_country, "Santiago, Chile")
        formatted_city_country = city_country("santiago", "chile", 1000)
        self.assertEqual(formatted_city_country, "Santiago, Chile - population 1000")

    def test_city_country_population(self):
        formatted_city_country = city_country("santiago", "chile", 5000000)
        self.assertEqual(formatted_city_country, "Santiago, Chile - population 5000000")


if __name__ == '__main__':
    unittest.main()
