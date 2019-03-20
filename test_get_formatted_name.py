from unittest import TestCase


class TestGet_formatted_name(TestCase):
    formatted_name = get_formatted_name('li', 'haining', 'humble')
    self.assertEqual(formatted_name, 'Li Humble Haining')
