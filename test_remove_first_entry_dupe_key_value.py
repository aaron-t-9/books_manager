"""
Unit test for remove_first_entry_dupe_key_value

Aaron T.
"""

from unittest import TestCase
from book_manager import remove_first_entry_dupe_key_value


class TestRemoveFirstEntryDupeKey(TestCase):

    def test_empty_list(self):
        test_book_collection = []
        expected_output = []
        actual_value = remove_first_entry_dupe_key_value(test_book_collection)
        self.assertEqual(expected_output, actual_value)

    def test_remove_first_entry_dupe_key_value_remover(self):
        test_book_collection = [{'author': 'author', 'title': 'title', 'publisher': 'publisher',
                                 'shelf': 'shelf', 'category': 'category', 'subject': 'subject'}]
        expected_output = []
        actual_value = remove_first_entry_dupe_key_value(test_book_collection)
        self.assertEqual(expected_output, actual_value)

    def test_remove_first_entry_dupe_key_value_valid_book(self):
        test_book_collection = [{'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego', 'category': 'Food',
                                 'subject': 'Sustenance'}]
        expected_output = [{'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego', 'category': 'Food',
                            'subject': 'Sustenance'}]
        actual_value = remove_first_entry_dupe_key_value(test_book_collection)
        self.assertEqual(expected_output, actual_value)

    def test_remove_first_entry_dupe_key_value_dupe_book_valid_book(self):
        test_book_collection = [{'author': 'author', 'title': 'title', 'publisher': 'publisher',
                                 'shelf': 'shelf', 'category': 'category', 'subject': 'subject'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego', 'category': 'Food',
                                 'subject': 'Sustenance'}]
        expected_output = [{'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego', 'category': 'Food',
                            'subject': 'Sustenance'}]
        actual_value = remove_first_entry_dupe_key_value(test_book_collection)
        self.assertEqual(expected_output, actual_value)

    def test_remove_first_entry_dupe_key_value_remover_dupe_book_second_index(self):
        test_book_collection = [{'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego', 'category': 'Food',
                                 'subject': 'Sustenance'},
                                {'author': 'author', 'title': 'title', 'publisher': 'publisher',
                                 'shelf': 'shelf', 'category': 'category',
                                 'subject': 'subject'}]
        expected_output = [{'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego', 'category': 'Food',
                            'subject': 'Sustenance'},
                           {'author': 'author', 'title': 'title', 'publisher': 'publisher',
                            'shelf': 'shelf', 'category': 'category',
                            'subject': 'subject'}]
        actual_value = remove_first_entry_dupe_key_value(test_book_collection)
        self.assertEqual(expected_output, actual_value)
