import unittest
from linear_search import *

class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_one_element_array_returns_correct_index_if_found(self):
        index = linear_search([1], 1)
        self.assertEqual(0, index)

    def test_one_element_array_returns_None_if_not_found(self):
        index = linear_search([1], 2)
        self.assertEqual(None, index)

    def test_two_element_array_returns_correct_index_if_found(self):
        index = linear_search([1, 2], 2)
        self.assertEqual(1, index)

    def test_two_element_array_returns_None_if_not_found(self):
        index = linear_search([1, 2], 3)
        self.assertEqual(None, index)

    def test_many_element_array_returns_correct_index_if_found(self):
        index = linear_search([2, 5, 8, 100, 9], 8)
        self.assertEqual(2, index)

    def test_many_element_array_returns_None_if_not_found(self):
        index = linear_search([2, 5, 8, 100, 9], 50)
        self.assertEqual(None, index)


if __name__ == '__main__':
  unittest.main()