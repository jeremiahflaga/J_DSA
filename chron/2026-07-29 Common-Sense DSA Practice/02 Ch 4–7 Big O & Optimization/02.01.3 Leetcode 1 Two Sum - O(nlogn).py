#####################
# Leetcode 1 Two Sum
# (see previous files)
#
# 4th attempt - will try an algorithm that is less than O(n^2) time complexity
#   - O(nlogn) 
#       - O(n) for creating array of tuples, 
#           O(nlogn) for sorting using built-in sort(), 
#           O(logn) for bisect_left() and for bisect_right(), 
#           and some constant time computations
#   - write on paper first
#
# Aug 19, 2026 
# Start: 10:14 PM (plus about 30 minutes of time spent this morning thinking about Hint 2 in the problem description)
#
# End: 11:04 PM 
# Result: WRONG answer (10 / 65 testcases passed)
# Test case on Leetcode: nums = [-1,-2,-3,-4,-5] , target = -8, expected output = [2,4], my output = [0,4]
# Submission Link: https://leetcode.com/problems/two-sum/submissions/2112839032/
#####################
#
# Kapoy pa man mangita og algorithm with less than O(n^2) time complexity.
# Brute force solution is already accepted, so will set this aside for now, and go solve other problems.
#


from bisect import bisect_left, bisect_right
from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        nums_tuple = []
        for index,value in enumerate(nums):
            nums_tuple.append((value,index))

        nums_tuple.sort()
        print("nums_tuple: ", nums_tuple)

        index_with_value_not_greater_than_target = bisect_right(nums_tuple, (target, len(nums)))        
        print("index_with_value_not_greater_than_target: ", index_with_value_not_greater_than_target)

        difference = target - nums_tuple[index_with_value_not_greater_than_target - 1][0]        
        print("difference: ", difference)

        index_with_value_not_less_than_difference = bisect_left(nums_tuple, (difference, 0))        
        print("index_with_value_not_less_than_difference: ", index_with_value_not_less_than_difference)
        
        output_index_1 = min(nums_tuple[index_with_value_not_less_than_difference][1], nums_tuple[index_with_value_not_greater_than_target - 1][1])
        output_index_2 = max(nums_tuple[index_with_value_not_less_than_difference][1], nums_tuple[index_with_value_not_greater_than_target - 1][1])
        return [output_index_1, output_index_2]



#####################

# class Tests(unittest.TestCase):
  
#     def __init__(self, *args, **kwargs):
#         unittest.TestCase.__init__(self, *args, **kwargs) 

#     def test_two_item_array(self):
#         soln = Solution()
#         result = soln.twoSum([1,2], 3)
#         self.assertEqual([0,1], result)

#     def test_three_item_array(self):
#         soln = Solution()
#         result = soln.twoSum([1,2,3], 4)
#         self.assertEqual([0,2], result)

#     def test_three_item_array_2nd_test(self):
#         soln = Solution()
#         result = soln.twoSum([1,2,3], 5)
#         self.assertEqual([1,2], result)

#     def test_four_item_array(self):
#         soln = Solution()
#         result = soln.twoSum([1,2,3,4], 6)
#         self.assertEqual([1,3], result)

#     def test_four_item_array_2nd_test(self):
#         soln = Solution()
#         result = soln.twoSum([1,2,3,4], 7)
#         self.assertEqual([2,3], result)

#     #####################################################

#     def test_example_1_from_problem_description(self):
#         soln = Solution()
#         result = soln.twoSum([2,7,11,15], 9)
#         self.assertEqual([0,1], result)

#     def test_example_2_from_problem_description(self):
#         soln = Solution()
#         result = soln.twoSum([3,2,4], 6)
#         self.assertEqual([1,2], result)

#     def test_example_3_from_problem_description(self):
#         soln = Solution()
#         result = soln.twoSum([3,3], 6)
#         self.assertEqual([0,1], result)

#     #####################################################

#     def test_with_zero(self):
#         soln = Solution()
#         result = soln.twoSum([0,6], 6)
#         self.assertEqual([0,1], result)

#     def test_with_zero_2nd_test(self):
#         soln = Solution()
#         result = soln.twoSum([1,0,6], 6)
#         self.assertEqual([1,2], result)

#     def test_with_zero_3rd_test(self):
#         soln = Solution()
#         result = soln.twoSum([0,4,6], 6)
#         self.assertEqual([0,2], result)

#     def test_negative_number(self):
#         soln = Solution()
#         result = soln.twoSum([-1,6], 5)
#         self.assertEqual([0,1], result)

#     def test_negative_number_2nd_test(self):
#         soln = Solution()
#         result = soln.twoSum([3,0,-1,6], 5)
#         self.assertEqual([2,3], result)

#     #####################################################

#     def test_zero_target(self):
#         soln = Solution()
#         result = soln.twoSum([-6,6], 0)
#         self.assertEqual([0,1], result)

#     def test_zero_target_2(self):
#         soln = Solution()
#         result = soln.twoSum([1,-6,6], 0)
#         self.assertEqual([1,2], result)

#     def test_negative_target(self):
#         soln = Solution()
#         result = soln.twoSum([1,-6,6], -5)
#         self.assertEqual([0,1], result)

#     def test_negative_target_2(self):
#         soln = Solution()
#         result = soln.twoSum([5,1,-6,6], -5)
#         self.assertEqual([1,2], result)

#     #####################################################

#     def test_for_case_which_failed_during_last_attempt(self):
#         soln = Solution()
#         result = soln.twoSum([0,4,3,0], 0)
#         self.assertEqual([0,3], result)

#####################

class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    # def test_example_2_from_problem_description(self):
    #     soln = Solution()
    #     result = soln.twoSum([3,2,4], 6)
    #     self.assertEqual([1,2], result)
    
    def test_negative_number_2nd_test(self):
        soln = Solution()
        result = soln.twoSum([3,0,-1,6], 5)
        self.assertEqual([2,3], result)




if __name__ == '__main__':
  unittest.main()
