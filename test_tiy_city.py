import unittest
from tiy_city_function import city_country_formatting

class test_city_country (unittest.TestCase):
    """testing the formatting of city country type of data"""
    def test_formatting_CityCountry(self):
        """formating test with city country"""
        formatted_duo=city_country_formatting('santiago', 'chile')
        self.assertEqual(formatted_duo, 'Santiago, Chile')

    def test_formatting_CityCountryPopulation (self):
        """formatting test with city country population"""
        formatted_trio=city_country_formatting('santiago','chile',5000000)
        self.assertEqual(formatted_trio,'Santiago, Chile, population: 5000000')

if __name__ == '__main__':
    unittest.main()