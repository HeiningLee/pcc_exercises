import unittest
from chapter11_name_function import get_formatted_name


class NameTestCase(unittest.TestCase):
    """ Test name_function.py"""

    def test_first_last_name(self):
        formatted_name = get_formatted_name('li', 'haining')
        self.assertEqual(formatted_name, 'Li Haining')

    def test_first_last_middle_name(self):
        formatted_name = get_formatted_name('li', 'haining', 'humble')
        self.assertEqual(formatted_name, 'Li Humble Haining')


if __name__ == '__main__':
    TestCase
# unittest.main
