#####################
# Leetcode 1 Two Sum
# https://leetcode.com/problems/two-sum/description/

# Aug 9, 2026
# Start: 11:05 PM

# Initial solution: 
#   - sort the array first 
#       (searched for Python built-in sort; it has .sort() which sorts a list in place)
#   - after sorting exclude those items greater than or equal to the target 
#       (searched for Python built in search sorted list - from bisect import bisect_left)
#       (you can use Python bisect_left to search for item or greater than item)
#   - 

# End: 11:30 PM
# Result: WRONG answer, because sorting the nums array in place destroys the original indices of the items
# Test case on Leetcode: nums = [3,2,4] , target = 6
#####################
#
# 2nd solution:
#   - need to find a way to preserve indices of the items in the array
#       ( you can create an array of tuples, (item, orig_index))


from bisect import bisect_left
from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums.sort()
        bisect_index = bisect_left(nums, target)
        # new_nums = nums[:bisect_index]

        i = 0        
        while i < bisect_index:
            j = i+1
            while j < bisect_index:
                if nums[i] + nums[j] == target:
                    return [i,j]                
                j = j+1
            i = i+1

        return []
        

#####################


class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_two_item_array(self):
        soln = Solution()
        result = soln.twoSum([1,2], 3)
        self.assertEqual([0,1], result)

    def test_three_item_array(self):
        soln = Solution()
        result = soln.twoSum([1,2,3], 4)
        self.assertEqual([0,2], result)

    def test_three_item_array_2nd_test(self):
        soln = Solution()
        result = soln.twoSum([1,2,3], 5)
        self.assertEqual([1,2], result)

    def test_four_item_array(self):
        soln = Solution()
        result = soln.twoSum([1,2,3,4], 6)
        self.assertEqual([1,3], result)

    def test_four_item_array_2nd_test(self):
        soln = Solution()
        result = soln.twoSum([1,2,3,4], 7)
        self.assertEqual([2,3], result)




if __name__ == '__main__':
  unittest.main()
