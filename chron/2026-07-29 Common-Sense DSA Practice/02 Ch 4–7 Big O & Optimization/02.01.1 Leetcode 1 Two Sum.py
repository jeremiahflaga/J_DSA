#####################
# Leetcode 1 Two Sum
# (see file for first attempt)
#
# 2nd attempt
# Aug 18, 2026
# Start: 10:20 PM
#
#   - need to find a way to preserve indices of the items in the array
#       ( you can create an array of tuples, (item, orig_index))
#
# End: 11:28 PM
# Result: WRONG answer again (54 / 65 testcases passed)
# Test case on Leetcode: nums = [0,4,3,0] , target = 0, expected output = [0,3], my output = [0,1]
# Submission Link: https://leetcode.com/problems/two-sum/submissions/2111609027/
#####################
# Reading Hints 1 and 2
#
# Hint 1
# A really brute force way would be to search for all possible pairs of numbers but that would be 
# too slow. Again, it's best to try out brute force solutions just for completeness. It is from 
# these brute force solutions that you can come up with optimizations.
#
# Hint 2
# So, if we fix one of the numbers, say x, we have to scan the entire array to find the next 
# number y which is value - x where value is the input parameter. Can we change our array somehow 
# so that this search becomes faster?
#
# Need to try brute force next time
# And after doing brute force, write solution on paper first

from bisect import bisect_left
from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # in python, can I sort list of tuples by first item in tuple?
        # Yes, you can easily sort a list of tuples by the first item. 
        # In fact, Python's built-in sorting mechanisms do this automatically by default.
        nums_tuple = []
        for index,value in enumerate(nums):
            nums_tuple.append((value,index))

        nums_tuple.sort()

        # does bisect_left work on list of tuples in python?
        # Yes...
        # Search using a partial tuple (e.g., just the first element)
        # Note: You must provide a dummy value for the missing tuple positions
        dummy_value = -float('inf')
        bisect_index = bisect_left(nums_tuple, (target,dummy_value))

        print("nums: ", nums)
        print("target: ", target)
        print("nums_tuple: ", nums_tuple)
        print("bisect_index: ", bisect_index)

        i = 0        
        while i < bisect_index:
            j = i+1
            while j < bisect_index:
                if nums_tuple[i][0] + nums_tuple[j][0] == target:
                    return [nums_tuple[i][1],nums_tuple[j][1]]                
                j = j+1
            i = i+1

        # return [0,1] for edge case where 
        return [0,1]



# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         # in python, can I sort list of tuples by first item in tuple?
#         # Yes, you can easily sort a list of tuples by the first item. 
#         # In fact, Python's built-in sorting mechanisms do this automatically by default.
#         nums_tuple = [] # array of tuples (value, index) of nums array
#         for index,value in enumerate(nums):
#             nums_tuple.append((value,index))

#         nums_tuple.sort()

#         # does bisect_left work on list of tuples in python?
#         # Yes...
#         # Search using a partial tuple (e.g., just the first element)
#         # Note: You must provide a dummy value for the missing tuple positions
#         dummy_value = -float('inf') # what dummy value should I use for int or number
#         bisect_index = bisect_left(nums_tuple, (target,dummy_value))

#         # If value at bisect_index is equal to target, increment bisect_index so that 
#         # the value at that index will be considered in the computation below
#         if nums_tuple[bisect_index][0] == target and bisect_index < len(nums) - 1:
#             bisect_index = bisect_index + 1

#         print("nums: ", nums)
#         print("target: ", target)
#         print("nums_tuple: ", nums_tuple)
#         print("bisect_index: ", bisect_index)

#         i = 0        
#         while i < bisect_index:
#             j = i+1

#             # if (j == len(nums_tuple) - 1): # for edge case where relevant value is the last item of the array
#             #     if nums_tuple[i][0] + nums_tuple[j][0] == target:
#             #         return [nums_tuple[i][1],nums_tuple[j][1]]
            
#             while j < bisect_index:
#                 print("i,j: ", i, ",", j)
#                 if nums_tuple[i][0] + nums_tuple[j][0] == target:
#                     return [nums_tuple[i][1],nums_tuple[j][1]]
#                 j = j+1
#             i = i+1

        
#         return []
        

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

    #####################################################

    def test_example_1_from_problem_description(self):
        soln = Solution()
        result = soln.twoSum([2,7,11,15], 9)
        self.assertEqual([0,1], result)

    def test_example_2_from_problem_description(self):
        soln = Solution()
        result = soln.twoSum([3,2,4], 6)
        self.assertEqual([1,2], result)

    def test_example_3_from_problem_description(self):
        soln = Solution()
        result = soln.twoSum([3,3], 6)
        self.assertEqual([0,1], result)

    #####################################################

    def test_with_zero(self):
        soln = Solution()
        result = soln.twoSum([0,6], 6)
        self.assertEqual([0,1], result)

    # def test_with_zero_2nd_test(self):
    #     soln = Solution()
    #     result = soln.twoSum([1,0,6], 6)
    #     self.assertEqual([1,2], result)

    # def test_with_zero_3rd_test(self):
    #     soln = Solution()
    #     result = soln.twoSum([0,4,6], 6)
    #     self.assertEqual([0,2], result)

    # def test_negative_number(self):
    #     soln = Solution()
    #     result = soln.twoSum([-1,6], 5)
    #     self.assertEqual([0,1], result)

    # def test_negative_number_2nd_test(self):
    #     soln = Solution()
    #     result = soln.twoSum([3,0,-1,6], 5)
    #     self.assertEqual([2,3], result)

    #####################################################

    # def test_zero_target(self):
    #     soln = Solution()
    #     result = soln.twoSum([-6,6], 0)
    #     self.assertEqual([0,1], result)

    # def test_zero_target_2(self):
    #     soln = Solution()
    #     result = soln.twoSum([1,-6,6], 0)
    #     self.assertEqual([1,2], result)

    # def test_negative_target(self):
    #     soln = Solution()
    #     result = soln.twoSum([1,-6,6], -5)
    #     self.assertEqual([0,1], result)

    # def test_negative_target_2(self):
    #     soln = Solution()
    #     result = soln.twoSum([5,1,-6,6], -5)
    #     self.assertEqual([1,2], result)





if __name__ == '__main__':
  unittest.main()
