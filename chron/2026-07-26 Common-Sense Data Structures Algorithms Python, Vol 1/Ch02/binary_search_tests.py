import unittest
from binary_search import *

class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_one_element_array_returns_correct_index_if_found(self):
        index = binary_search([1], 1)
        self.assertEqual(0, index)

    def test_one_element_array_returns_None_if_not_found(self):
        index = binary_search([1], 2)
        self.assertEqual(None, index)

    #####

    def test_two_element_array_returns_correct_index_if_found(self):
        index = binary_search([1, 2], 1)
        self.assertEqual(0, index)

    def test_two_element_array_returns_correct_index_if_found_2(self):
        index = binary_search([1, 2], 2)
        self.assertEqual(1, index)

    def test_two_element_array_returns_None_if_not_found(self):
        index = binary_search([1, 2], 3)
        self.assertEqual(None, index)

    #####
    
    def test_odd_length_array_first_element(self):
        index = binary_search([2, 5, 8, 9, 100], 2)
        self.assertEqual(0, index)

    def test_odd_length_array_last_element(self):
        index = binary_search([2, 5, 8, 9, 100], 100)
        self.assertEqual(4, index)

    def test_odd_length_array_middle_element(self):
        index = binary_search([2, 5, 8, 9, 100], 8)
        self.assertEqual(2, index)

    def test_odd_length_array_missing_element(self):
        index = binary_search([2, 5, 8, 9, 100], 50)
        self.assertEqual(None, index)

    #####
    
    def test_even_length_array_first_element(self):
        index = binary_search([2, 5, 9, 100], 2)
        self.assertEqual(0, index)

    def test_odd_length_array_last_element(self):
        index = binary_search([2, 5, 9, 100], 100)
        self.assertEqual(3, index)

    def test_odd_length_array_middle_element(self):
        index = binary_search([2, 5, 9, 100], 5)
        self.assertEqual(1, index)

    def test_odd_length_array_middle_element_2(self):
        index = binary_search([2, 5, 9, 100], 9)
        self.assertEqual(2, index)

    def test_odd_length_array_missing_element(self):
        index = binary_search([2, 5, 9, 100], 50)
        self.assertEqual(None, index)



if __name__ == '__main__':
  unittest.main()