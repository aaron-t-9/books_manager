"""
Unit test for move_book

Aaron T.
"""

from unittest import TestCase
from unittest.mock import patch
import io
from book_manager import move_book


class TestMoveBook(TestCase):

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_first_index(self, mock_stdout):
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
        search_results = [{'author': 'Julier',
                           'title': 'The Thames and Hudson Encyclopaedia of 20th Century Design '
                                    'and Designers', 'publisher': 'Thames & Hudson',
                           'shelf': '17', 'category': 'Art', 'subject': 'Design'},
                          {'author': 'Cox et al', 'title': 'The Sinmon & Schuster Encyclopedia '
                                                           'of Dinosaurs & Prehistoric Creatures',
                           'publisher': 'Simon & Schuster', 'shelf': '25', 'category': 'Biology',
                           'subject': 'Zoology'}]
        book_to_move = 1
        new_location = "Lego"
        move_book(book_collection_test, search_results, book_to_move, new_location)
        expected_output = "\n\033[1m" "The book 'The Thames and Hudson Encyclopaedia of 20th \
Century Design and Designers' by Julier has \
been moved from the shelf/location: 17, to the shelf/location: Lego." "\033[0m\n\n"
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_different_index(self, mock_stdout):
        book_collection_test = (
            {'author': 'Tzonis',
             'title': 'Santiago Calatrava The Complete Works Expanded Edition',
             'publisher': 'Rizzoli', 'shelf': '12', 'category': 'Architecture',
             'subject': '20th Century'},
            {'author': 'Julier',
             'title': 'The Thames and Hudson Encyclopaedia of 20th Century Design and Designers',
             'publisher': 'Thames & Hudson', 'shelf': '17', 'category': 'Art',
             'subject': 'Design'},
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
        search_results = [{'author': 'Whitfield', 'title': 'The Simon & Schuster Encyclopedia of '
                                                           'Animals',
                           'publisher': 'Simon & Schuster', 'shelf': '25',
                           'category': 'Biology', 'subject': 'Zoology'},
                          {'author': 'Downs (ed)', 'title': 'Incredible Rogers Pass',
                           'publisher': 'Heritage House Publishing', 'shelf': '16',
                           'category': 'Geography', 'subject': 'Canadian'}]
        book_to_move = 2
        new_location = "13"
        move_book(book_collection_test, search_results, book_to_move, new_location)
        expected_output = "\n\033[1m" "The book 'Incredible Rogers Pass' by Downs (ed) has \
been moved from the shelf/location: 16, to the shelf/location: 13." "\033[0m\n\n"
        self.assertEqual(expected_output, mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_invalid_location(self, mock_stdout):
        book_collection_test = (
            {'author': 'Tzonis',
             'title': 'Santiago Calatrava The Complete Works Expanded Edition',
             'publisher': 'Rizzoli', 'shelf': '12', 'category': 'Architecture',
             'subject': '20th Century'},
            {'author': 'Julier',
             'title': 'The Thames and Hudson Encyclopaedia of 20th Century Design and Designers',
             'publisher': 'Thames & Hudson', 'shelf': '17', 'category': 'Art',
             'subject': 'Design'},
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
        search_results = [{'author': 'Whitfield', 'title': 'The Simon & Schuster Encyclopedia of '
                                                           'Animals',
                           'publisher': 'Simon & Schuster', 'shelf': '25',
                           'category': 'Biology', 'subject': 'Zoology'},
                          {'author': 'Downs (ed)', 'title': 'Incredible Rogers Pass',
                           'publisher': 'Heritage House Publishing', 'shelf': '16',
                           'category': 'Geography', 'subject': 'Canadian'}]
        book_to_move = 2
        new_location = "invalid"
        move_book(book_collection_test, search_results, book_to_move, new_location)
        expected_output = "\nInvalid location selected.\n\n"
        self.assertEqual(expected_output, mock_stdout.getvalue())
