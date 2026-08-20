#####################
# Leetcode 268 Missing Number
# https://leetcode.com/problems/missing-number/description/

# Aug 20, 2026
# Start: 9:17 PM

# Initial solution: 
#   - Use a bitarray. Iterate through the nums array, then for each number in the array
#       set the corresponding index in the bitarray to 1.
#       Then use necessary bit manipulation to get the value for the missing number
#       
#   Is there a built-in bit array in python?
#       No.
#   
#   

# End: 9:41 PM
# Submission Link: https://leetcode.com/problems/missing-number/submissions/2113981778/
#####################


from typing import List
import unittest

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_exists_array = [False] * (len(nums) + 1)

        for i in nums:
            num_exists_array[i] = True

        for i in range(0, len(num_exists_array)):
            if num_exists_array[i] == False:
                return i

        

#####################


class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_1(self):
        soln = Solution()
        result = soln.missingNumber([3,0,1])
        self.assertEqual(2, result)

    def test_2(self):
        soln = Solution()
        result = soln.missingNumber([0,1])
        self.assertEqual(2, result)

    def test_3(self):
        soln = Solution()
        result = soln.missingNumber([9,6,4,2,3,5,7,0,1])
        self.assertEqual(8, result)



if __name__ == '__main__':
  unittest.main()
