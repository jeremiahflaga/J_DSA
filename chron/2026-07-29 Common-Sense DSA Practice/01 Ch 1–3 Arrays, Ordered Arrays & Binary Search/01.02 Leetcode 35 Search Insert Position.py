from typing import List
import unittest

# is there a List type in Python?
# The list Type Hint (Design Time)
#   Modern Python (3.9 and newer): list[int]
#   Older Python (3.8 and below): from typing import List, List[int]


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if len(nums) == 0:
            return 0
        
        lower_bound = 0
        upper_bound = len(nums) - 1

        while lower_bound <= upper_bound:
            midpoint = (lower_bound + upper_bound) // 2
            val_at_mid = nums[midpoint]

            if target == val_at_mid:
                return midpoint
            elif target < val_at_mid:
                upper_bound = midpoint - 1
            elif target > val_at_mid:
                lower_bound = midpoint + 1

        return lower_bound


class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_empty(self):
        soln = Solution()
        index = soln.searchInsert([], 1)
        self.assertEqual(0, index)

    ###################
    # one item array
    ###################

    def test_one_item_array_search_for_existing(self):
        soln = Solution()
        index = soln.searchInsert([1], 1)
        self.assertEqual(0, index)

    def test_one_item_array_search_for_nonexisting_insert_at_beginning(self):
        soln = Solution()
        index = soln.searchInsert([1], 0)
        self.assertEqual(0, index)

    def test_one_item_array_search_for_nonexisting_insert_at_end(self):
        soln = Solution()
        index = soln.searchInsert([1], 2)
        self.assertEqual(1, index)

    ###################
    # two item array    
    ###################

    def test_two_item_array_search_for_existing_1(self):
        soln = Solution()
        index = soln.searchInsert([1,2], 1)
        self.assertEqual(0, index)

    def test_two_item_array_search_for_existing_2(self):
        soln = Solution()
        index = soln.searchInsert([1,2], 2)
        self.assertEqual(1, index)

    def test_two_item_array_search_for_nonexisting_insert_at_beginning(self):
        soln = Solution()
        index = soln.searchInsert([1,2], 0)
        self.assertEqual(0, index)

    def test_two_item_array_search_for_nonexisting_insert_at_end(self):
        soln = Solution()
        index = soln.searchInsert([1,2], 3)
        self.assertEqual(2, index)

    def test_two_item_array_search_for_nonexisting_insert_in_middle(self):
        soln = Solution()
        index = soln.searchInsert([1,4], 2)
        self.assertEqual(1, index)

    ###################
    # three  item array    
    ###################

    def test_three_item_array_search_for_nonexisting_insert_in_middle(self):
        soln = Solution()
        index = soln.searchInsert([1,4,7], 5)
        self.assertEqual(2, index)


    # def test_existing(self):
    #     soln = Solution()
    #     index = soln.searchInsert([1,3,5,6], 5)
    #     self.assertEqual(2, index)

    # def test_non_existing_insert_at_beginning(self):
    #     soln = Solution()
    #     index = soln.searchInsert([1,3,5,6], 0)
    #     self.assertEqual(0, index)

    # def test_non_existing_insert_at_end(self):
    #     soln = Solution()
    #     index = soln.searchInsert([1,3,5,6], 7)
    #     self.assertEqual(4, index)

if __name__ == '__main__':
  unittest.main()


#####################
# Leetcode 35 Search Insert Position
# July 30, 2026
# Start: 10:11 PM
# End: 10:38 PM
# Submission Link: https://leetcode.com/problems/search-insert-position/submissions/2087632004/
#####################