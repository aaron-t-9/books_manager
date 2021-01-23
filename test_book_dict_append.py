"""
Unit test for book_dict_append

Aaron T.
"""

from unittest import TestCase
from book_manager import book_dict_append


class TestBookDictAppend(TestCase):

    def test_empty(self):
        temp_list = []
        expected_output = ()
        actual_value = book_dict_append(temp_list)
        self.assertEqual(expected_output, actual_value)

    def test_one_book(self):
        temp_list = [['Steven Jobs', 'Apple and Oranges', 'Gill Bates', 'Noguchi',
                      'Technology', 'Critique']]
        expected_output = ({'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'Gill Bates', 'shelf': 'Noguchi',
                            'category': 'Technology', 'subject': 'Critique'},)
        actual_value = book_dict_append(temp_list)
        self.assertEqual(expected_output, actual_value)

    def test_two_books(self):
        temp_list = [['Frame', 'Yellow Flowers in the Antipodean Room', 'George Braziller', '4',
                      'Literature', 'English'], ['Rozanov', 'Probability Theory: A Concise Course',
                                                 'Dover', 'Island', 'Mathematics', 'Probability']]

        expected_output = ({'author': 'Frame', 'title': 'Yellow Flowers in the Antipodean Room',
                            'publisher': 'George Braziller', 'shelf': '4',
                            'category': 'Literature', 'subject': 'English'},
                           {'author': 'Rozanov', 'title': 'Probability Theory: A Concise Course',
                            'publisher': 'Dover', 'shelf': 'Island', 'category': 'Mathematics',
                            'subject': 'Probability'})
        actual_value = book_dict_append(temp_list)
        self.assertEqual(expected_output, actual_value)
