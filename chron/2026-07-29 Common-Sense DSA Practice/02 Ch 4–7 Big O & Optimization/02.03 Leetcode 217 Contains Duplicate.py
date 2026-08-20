#####################
# Leetcode 217 Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/description/

# Aug 20, 2026
# Start: 9:44 PM

# Initial solution: 
#   Use hash table / dictionary
#   

# End: 9:53 PM
# Submission Link: https://leetcode.com/problems/contains-duplicate/submissions/2113994620/
#####################


from typing import List
import unittest

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_exists_dict = {}

        for i in nums:
            if num_exists_dict.get(i) == True:
                return True
            
            num_exists_dict[i] = True

        return False
        

        

#####################


class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_1(self):
        soln = Solution()
        result = soln.containsDuplicate([1,2,3,1])
        self.assertEqual(True, result)

    def test_2(self):
        soln = Solution()
        result = soln.containsDuplicate([1,2,3,4])
        self.assertEqual(False, result)

    def test_3(self):
        soln = Solution()
        result = soln.containsDuplicate([1,1,1,3,3,4,3,2,4,2])
        self.assertEqual(True, result)



if __name__ == '__main__':
  unittest.main()
