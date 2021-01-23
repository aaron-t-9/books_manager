"""
Unit test for search_engine

Aaron T.
"""

from unittest import TestCase
from book_manager import search_engine


class TestSearchEngine(TestCase):

    def test_empty_search_by_author(self):
        book_collection_test = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                                 'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                                 'subject': 'Automobile'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'}]
        key = "author"
        search_query = ""
        expected_output = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                            'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                            'subject': 'Automobile'},
                           {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'},
                           {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '12',
                            'category': 'Technology', 'subject': 'Biography'}]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)

    def test_empty_search_by_subject(self):
        book_collection_test = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                                 'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                                 'subject': 'Automobile'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'}]
        key = "subject"
        search_query = ""
        expected_output = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                            'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                            'subject': 'Automobile'},
                           {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'},
                           {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '12',
                            'category': 'Technology', 'subject': 'Biography'}]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)

    def test_empty_search_by_shelf(self):
        book_collection_test = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                                 'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                                 'subject': 'Automobile'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'}]
        key = "shelf"
        search_query = ""
        expected_output = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                            'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                            'subject': 'Automobile'},
                           {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'},
                           {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '12',
                            'category': 'Technology', 'subject': 'Biography'}]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)

    def test_full_query_search_by_author(self):
        book_collection_test = ({'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '33',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'})
        key = "author"
        search_query = "tzonis"
        expected_output = [{'author': 'Tzonis',
                            'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                            'publisher': 'Rizzoli', 'shelf': '33',
                            'category': 'Architecture', 'subject': '20th Century'}]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)

    def test_partial_query_search_by_author(self):
        book_collection_test = ({'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '33',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'})
        key = "author"
        search_query = "en"
        expected_output = [{'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'},
                           {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '12',
                            'category': 'Technology', 'subject': 'Biography'}]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)

    def test_full_query_search_by_title(self):
        book_collection_test = ({'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '33',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'})
        key = "title"
        search_query = "top ramen"
        expected_output = [{'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'}]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)

    def test_partial_query_search_by_title(self):
        book_collection_test = ({'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '33',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'})
        key = "title"
        search_query = "e"
        expected_output = [{'author': 'Tzonis',
                            'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                            'publisher': 'Rizzoli', 'shelf': '33',
                            'category': 'Architecture', 'subject': '20th Century'},
                           {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'},
                           {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '12',
                            'category': 'Technology', 'subject': 'Biography'}]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)

    def test_full_query_search_by_shelf(self):
        book_collection_test = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                                 'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                                 'subject': 'Automobile'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'}]
        key = "shelf"
        search_query = "12"
        expected_output = [{'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '12',
                            'category': 'Technology', 'subject': 'Biography'}]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)

    def test_partial_query_search_by_shelf(self):
        book_collection_test = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                                 'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                                 'subject': 'Automobile'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'}]
        key = "shelf"
        search_query = "1"
        expected_output = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                            'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                            'subject': 'Automobile'},
                           {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                            'publisher': 'California', 'shelf': '12',
                            'category': 'Technology', 'subject': 'Biography'}]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)

    def test_full_query_search_by_subject(self):
        book_collection_test = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                                 'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                                 'subject': 'Automobile'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'}]
        key = "subject"
        search_query = "automobile"
        expected_output = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                            'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                            'subject': 'Automobile'}, ]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)

    def test_partial_query_search_by_subject(self):
        book_collection_test = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                                 'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                                 'subject': 'Automobile'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '12',
                                 'category': 'Technology', 'subject': 'Biography'}]
        key = "subject"
        search_query = "t"
        expected_output = [{'author': 'Mazda', 'title': "2008 Mazda MX-5 Owner's Manual",
                            'publisher': 'Mazda', 'shelf': '17', 'category': 'Science',
                            'subject': 'Automobile'},
                           {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                            'publisher': 'Nong Shim', 'shelf': 'Lego',
                            'category': 'Food', 'subject': 'Sustenance'}]
        actual_value = search_engine(book_collection_test, key, search_query)
        self.assertEqual(expected_output, actual_value)
