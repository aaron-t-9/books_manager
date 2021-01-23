"""
Unit test for is_valid_location

Aaron T.
"""

from unittest import TestCase
from unittest.mock import patch
from book_manager import is_valid_location


class TestIsValidLocation(TestCase):

    @patch('builtins.input', side_effect=[''])
    def test_empty(self, mock_output):
        valid_locations = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2',
                           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30',
                           '31', '32', '33', '34', '35', '36', '37', '38', '4', '5', '6', '7', '8',
                           '9', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
        expected_output = 'invalid'
        actual_value = is_valid_location(valid_locations)
        self.assertEqual(expected_output, actual_value)

    @patch('builtins.input', side_effect=['noguchi'])
    def test_valid_location(self, mock_output):
        valid_locations = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2',
                           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30',
                           '31', '32', '33', '34', '35', '36', '37', '38', '4', '5', '6', '7', '8',
                           '9', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
        expected_output = 'Noguchi'
        actual_value = is_valid_location(valid_locations)
        self.assertEqual(expected_output, actual_value)

    @patch('builtins.input', side_effect=['read in g'])
    def test_invalid_location(self, mock_output):
        valid_locations = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2',
                           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30',
                           '31', '32', '33', '34', '35', '36', '37', '38', '4', '5', '6', '7', '8',
                           '9', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
        expected_output = 'invalid'
        actual_value = is_valid_location(valid_locations)
        self.assertEqual(expected_output, actual_value)

    @patch('builtins.input', side_effect=['0'])
    def test_int_invalid_location(self, mock_output):
        valid_locations = ['1', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '2',
                           '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '3', '30',
                           '31', '32', '33', '34', '35', '36', '37', '38', '4', '5', '6', '7', '8',
                           '9', 'Gaby', 'Island', 'Lego', 'Noguchi', 'Reading', 'Students']
        expected_output = 'invalid'
        actual_value = is_valid_location(valid_locations)
        self.assertEqual(expected_output, actual_value)
