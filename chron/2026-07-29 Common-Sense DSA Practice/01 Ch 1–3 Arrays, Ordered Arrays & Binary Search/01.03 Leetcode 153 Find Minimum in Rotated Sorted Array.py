#####################
# Leetcode 153 Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

# Aug 4, 2026
# Start: 10:07 PM

# Initial solution: 
#  - use binary search
#  - for each value in midpoint, peek its neighboring items, 
#       and check if greater/lesser than the mid value

# End: 10:52 PM
# Submission Link: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/2094147667/
#####################

from typing import List
import unittest


class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums_length = len(nums) - 1
        value_at_init_index = nums[0]
        value_at_final_index = nums[nums_length]

        # optimization: if at the start, the value at index zero is lesser than the value
        # at the last index, then the value at zero is the minimum value
        if value_at_init_index <= value_at_final_index:
            return value_at_init_index

        lower_bound = 0
        upper_bound = nums_length

        while (lower_bound <= upper_bound):
            midpoint = (lower_bound + upper_bound) // 2
            value_at_midpoint = nums[midpoint]

            # is_mid_init_index = mid == 0
            # is_mid_final_index = mid == length
            right_neighbor_value = value_at_midpoint
            left_neighbor_value = value_at_midpoint
            
            if midpoint < nums_length:
                right_neighbor_value = nums[midpoint + 1]

                # if RIGHT neighbor is less than midpoint value, that means you found 
                # that min value of the sorted array before the rotation was made
                if (value_at_midpoint > right_neighbor_value):
                    return right_neighbor_value
                
            if midpoint > 0:
                left_neighbor_value = nums[midpoint - 1]

                # if LEFT neighbor is greater than midpoint value, that means you found 
                # that min value of the sorted array before the rotation was made: 
                # the min is the value at the midpoint
                if (left_neighbor_value > value_at_midpoint):
                    return value_at_midpoint

            # Observation: the input array, nums, has this property where if it is rotated,
            # then the value at index zero is greater than the value at the final index

            if value_at_midpoint > value_at_init_index:
                # scan the right half of the array because the min value can be found in there
                lower_bound = midpoint + 1

            if value_at_midpoint < value_at_init_index:
                upper_bound = midpoint - 1

        return nums[lower_bound]


#####################


class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_one_item_array(self):
        soln = Solution()
        min_value = soln.findMin([1])
        self.assertEqual(1, min_value)

    def test_two_item_array_unrotated(self):
        soln = Solution()
        min_value = soln.findMin([1, 2])
        self.assertEqual(1, min_value)

    def test_two_item_array_rotated(self):
        soln = Solution()
        min_value = soln.findMin([2, 1])
        self.assertEqual(1, min_value)

    def test_three_item_array_unrotated(self):
        soln = Solution()
        min_value = soln.findMin([1, 2, 3])
        self.assertEqual(1, min_value)

    def test_three_item_array_rotated_once(self):
        soln = Solution()
        min_value = soln.findMin([3, 1, 2])
        self.assertEqual(1, min_value)

    def test_three_item_array_rotated_twice(self):
        soln = Solution()
        min_value = soln.findMin([2, 3, 1])
        self.assertEqual(1, min_value)

    def test_four_item_array_unrotated(self):
        soln = Solution()
        min_value = soln.findMin([-2, -1, 1, 2])
        self.assertEqual(-2, min_value)

    def test_four_item_array_rotated_thrice(self):
        soln = Solution()
        min_value = soln.findMin([-1, 1, 2, -2,])
        self.assertEqual(-2, min_value)



if __name__ == '__main__':
  unittest.main()
