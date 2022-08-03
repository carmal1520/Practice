import unittest
from city_functions import city_country

class NameTest(unittest.TestCase):

    def test_city_country(self):
        full_name = city_country('Virginia Beach', 'United States', population=15)
        self.assertEqual(full_name, 'Virginia Beach, United States Population-15')

if __name__ == '__main__':
    unittest.main()