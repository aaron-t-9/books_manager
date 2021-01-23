"""
Unit test for book_collection_empty_value_checker

Aaron T.
"""

from unittest import TestCase
from books import book_collection_empty_value_checker


class TestBookCollectionEmptyValueChecker(TestCase):

    def test_empty(self):
        book_collection_test = []
        expected_output = []
        actual_value = book_collection_empty_value_checker(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_single_book_empty_shelf(self):
        book_collection_test = [{'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '',
                                 'category': 'Architecture', 'subject': '20th Century'}]
        expected_output = [{'author': 'Tzonis',
                            'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                            'publisher': 'Rizzoli', 'shelf': 'None', 'category': 'Architecture',
                            'subject': '20th Century'}]
        actual_value = book_collection_empty_value_checker(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_single_book_empty_publisher(self):
        book_collection_test = [{'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': '', 'shelf': '12',
                                 'category': 'Architecture', 'subject': '20th Century'}]
        expected_output = [{'author': 'Tzonis',
                            'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                            'publisher': 'None', 'shelf': '12', 'category': 'Architecture',
                            'subject': '20th Century'}]
        actual_value = book_collection_empty_value_checker(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_single_book_empty_subject(self):
        book_collection_test = [{'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '12',
                                 'category': 'Architecture', 'subject': ''}]
        expected_output = [{'author': 'Tzonis',
                            'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                            'publisher': 'Rizzoli', 'shelf': '12', 'category': 'Architecture',
                            'subject': 'None'}]
        actual_value = book_collection_empty_value_checker(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_three_books_all_categories_empty(self):
        book_collection_test = [{'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '33',
                                 'category': '', 'subject': '20th Century'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': '', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '2',
                                 'category': '', 'subject': 'Biography'}]
        expected_output = [{'author': 'Tzonis',
                            'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                            'publisher': 'Rizzoli', 'shelf': '33',
                            'category': 'None', 'subject': '20th Century'},
                           {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'None', 'subject': 'Sustenance'},
                           {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '2',
                            'category': 'None', 'subject': 'Biography'}]
        actual_value = book_collection_empty_value_checker(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_three_books_one_category_empty(self):
        book_collection_test = [{'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '33',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '2',
                                 'category': '', 'subject': 'Biography'}]
        expected_output = [{'author': 'Tzonis',
                            'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                            'publisher': 'Rizzoli', 'shelf': '33',
                            'category': 'Architecture', 'subject': '20th Century'},
                           {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'},
                           {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '2',
                            'category': 'None', 'subject': 'Biography'}]
        actual_value = book_collection_empty_value_checker(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_three_books_all_authors_empty(self):
        book_collection_test = [{'author': '',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '33',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': '', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': '', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '2',
                                 'category': 'Technology', 'subject': 'Biography'}]
        expected_output = [{'author': 'None',
                            'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                            'publisher': 'Rizzoli', 'shelf': '33',
                            'category': 'Architecture', 'subject': '20th Century'},
                           {'author': 'None', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'},
                           {'author': 'None', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '2',
                            'category': 'Technology', 'subject': 'Biography'}]
        actual_value = book_collection_empty_value_checker(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_three_books_two_authors_empty(self):
        book_collection_test = [{'author': '',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '33',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': '', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '2',
                                 'category': 'Technology', 'subject': 'Biography'}]
        expected_output = [{'author': 'None',
                            'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                            'publisher': 'Rizzoli', 'shelf': '33',
                            'category': 'Architecture', 'subject': '20th Century'},
                           {'author': 'None', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'},
                           {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '2',
                            'category': 'Technology', 'subject': 'Biography'}]
        actual_value = book_collection_empty_value_checker(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_three_books_author_and_subject_empty(self):
        book_collection_test = [{'author': '',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '33',
                                 'category': 'Architecture', 'subject': ''},
                                {'author': '', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': '', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '2',
                                 'category': 'Technology', 'subject': ''}]
        expected_output = [{'author': 'None',
                            'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                            'publisher': 'Rizzoli', 'shelf': '33',
                            'category': 'Architecture', 'subject': 'None'},
                           {'author': 'None', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'},
                           {'author': 'None', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '2',
                            'category': 'Technology', 'subject': 'None'}]
        actual_value = book_collection_empty_value_checker(book_collection_test)
        self.assertEqual(expected_output, actual_value)
