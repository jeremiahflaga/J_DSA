#####################
# Leetcode 1 Two Sum
# (see files for first and second attempts)
#
# 3rd attempt - brute force, as suggested by Hint 1 in the problem description
# Aug 19, 2026
# Start: 10:01 PM
#
# End: 10:05 PM - too fast because AI gave suggestions for the nested for loop
# Result: Accepted - Never considered a brute force solution, because I thought I will get Time Limit error, 
#           or something like that if I use brute force, and that I will need to reimplement it in C++. 
#           Their test cases must not be that big for this problem, and so brute force works.
# Submission Link: https://leetcode.com/problems/two-sum/submissions/2112771963/
#####################


from bisect import bisect_left
from typing import List
import unittest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

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

    def test_with_zero_2nd_test(self):
        soln = Solution()
        result = soln.twoSum([1,0,6], 6)
        self.assertEqual([1,2], result)

    def test_with_zero_3rd_test(self):
        soln = Solution()
        result = soln.twoSum([0,4,6], 6)
        self.assertEqual([0,2], result)

    def test_negative_number(self):
        soln = Solution()
        result = soln.twoSum([-1,6], 5)
        self.assertEqual([0,1], result)

    def test_negative_number_2nd_test(self):
        soln = Solution()
        result = soln.twoSum([3,0,-1,6], 5)
        self.assertEqual([2,3], result)

    #####################################################

    def test_zero_target(self):
        soln = Solution()
        result = soln.twoSum([-6,6], 0)
        self.assertEqual([0,1], result)

    def test_zero_target_2(self):
        soln = Solution()
        result = soln.twoSum([1,-6,6], 0)
        self.assertEqual([1,2], result)

    def test_negative_target(self):
        soln = Solution()
        result = soln.twoSum([1,-6,6], -5)
        self.assertEqual([0,1], result)

    def test_negative_target_2(self):
        soln = Solution()
        result = soln.twoSum([5,1,-6,6], -5)
        self.assertEqual([1,2], result)

    #####################################################

    def test_for_case_which_failed_during_last_attempt(self):
        soln = Solution()
        result = soln.twoSum([0,4,3,0], 0)
        self.assertEqual([0,3], result)





if __name__ == '__main__':
  unittest.main()
