"""
Unit test for get_valid_location

Aaron T.
"""

from unittest import TestCase
from book_manager import get_valid_location


class TestGetValidLocation(TestCase):

    def test_empty_list(self):
        book_collection_test = ()
        expected_output = []
        actual_value = get_valid_location(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_empty_shelves(self):
        book_collection_test = (
            {'author': 'Tzonis', 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
             'publisher': 'Rizzoli', 'shelf': 'None', 'category': 'Architecture',
             'subject': '20th Century'},
            {'author': 'Julier',
             'title': 'The Thames and Hudson Encyclopaedia of 20th Century Design and Designers',
             'publisher': 'Thames & Hudson', 'shelf': 'None', 'category': 'Art',
             'subject': 'Design'},
            {'author': 'Cox et al',
             'title': 'The Sinmon & Schuster Encyclopedia of Dinosaurs & Prehistoric Creatures',
             'publisher': 'Simon & Schuster', 'shelf': 'None', 'category': 'Biology',
             'subject': 'Zoology'},
            {'author': 'Whitfield', 'title': 'The Simon & Schuster Encyclopedia of Animals',
             'publisher': 'Simon & Schuster', 'shelf': 'None', 'category': 'Biology',
             'subject': 'Zoology'},
            {'author': 'Downs (ed)', 'title': 'Incredible Rogers Pass',
             'publisher': 'Heritage House Publishing', 'shelf': 'None', 'category': 'Geography',
             'subject': 'Canadian'})
        expected_output = ['None']
        actual_value = get_valid_location(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_overlapping_shelves(self):
        book_collection_test = (
            {'author': 'Tzonis', 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
             'publisher': 'Rizzoli', 'shelf': 'Noguchi', 'category': 'Architecture',
             'subject': '20th Century'},
            {'author': 'Julier',
             'title': 'The Thames and Hudson Encyclopaedia of 20th Century Design and Designers',
             'publisher': 'Thames & Hudson', 'shelf': 'Noguchi', 'category': 'Art',
             'subject': 'Design'},
            {'author': 'Cox et al',
             'title': 'The Sinmon & Schuster Encyclopedia of Dinosaurs & Prehistoric Creatures',
             'publisher': 'Simon & Schuster', 'shelf': 'Noguchi', 'category': 'Biology',
             'subject': 'Zoology'},
            {'author': 'Whitfield', 'title': 'The Simon & Schuster Encyclopedia of Animals',
             'publisher': 'Simon & Schuster', 'shelf': 'Noguchi', 'category': 'Biology',
             'subject': 'Zoology'},
            {'author': 'Downs (ed)', 'title': 'Incredible Rogers Pass',
             'publisher': 'Heritage House Publishing', 'shelf': 'Noguchi', 'category': 'Geography',
             'subject': 'Canadian'})
        expected_output = ['Noguchi']
        actual_value = get_valid_location(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_numbered_shelves(self):
        book_collection_test = (
            {'author': 'Tzonis', 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
             'publisher': 'Rizzoli', 'shelf': '12', 'category': 'Architecture',
             'subject': '20th Century'},
            {'author': 'Julier',
             'title': 'The Thames and Hudson Encyclopaedia of 20th Century Design and Designers',
             'publisher': 'Thames & Hudson', 'shelf': '17', 'category': 'Art', 'subject': 'Design'},
            {'author': 'Cox et al',
             'title': 'The Sinmon & Schuster Encyclopedia of Dinosaurs & Prehistoric Creatures',
             'publisher': 'Simon & Schuster', 'shelf': '25', 'category': 'Biology',
             'subject': 'Zoology'},
            {'author': 'Whitfield', 'title': 'The Simon & Schuster Encyclopedia of Animals',
             'publisher': 'Simon & Schuster', 'shelf': '25', 'category': 'Biology',
             'subject': 'Zoology'},
            {'author': 'Downs (ed)', 'title': 'Incredible Rogers Pass',
             'publisher': 'Heritage House Publishing', 'shelf': '16', 'category': 'Geography',
             'subject': 'Canadian'})
        expected_output = ['12', '16', '17', '25']
        actual_value = get_valid_location(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_string_non_overlap_shelves(self):
        book_collection_test = ({'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': 'Students',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Lego',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': 'Gaby',
                                 'category': 'Technology', 'subject': 'Biography'})
        expected_output = ['Gaby', 'Lego', 'Students']
        actual_value = get_valid_location(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_string_with_overlap_shelves(self):
        book_collection_test = ({'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': 'Students',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': 'Gaby',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': 'Gaby',
                                 'category': 'Technology', 'subject': 'Biography'})
        expected_output = ['Gaby', 'Students']
        actual_value = get_valid_location(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_numbered_and_string_no_overlap_shelves(self):
        book_collection_test = ({'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '3',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': '12',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': 'Island',
                                 'category': 'Technology', 'subject': 'Biography'})
        expected_output = ['12', '3', 'Island']
        actual_value = get_valid_location(book_collection_test)
        self.assertEqual(expected_output, actual_value)

    def test_numbered_and_with_overlap_shelves(self):
        book_collection_test = ({'author': 'Tzonis',
                                 'title': 'Santiago Calatrava The Complete Works Expanded Edition',
                                 'publisher': 'Rizzoli', 'shelf': '3',
                                 'category': 'Architecture', 'subject': '20th Century'},
                                {'author': 'Ramen Noodles', 'title': 'Top Ramen',
                                 'publisher': 'Nong Shim', 'shelf': '13',
                                 'category': 'Food', 'subject': 'Sustenance'},
                                {'author': 'Steven Jobs', 'title': 'Apple and Oranges',
                                 'publisher': 'California', 'shelf': '3',
                                 'category': 'Technology', 'subject': 'Biography'})
        expected_output = ['13', '3']
        actual_value = get_valid_location(book_collection_test)
        self.assertEqual(expected_output, actual_value)
