#####################
# Leetcode 347 Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/

# Oct 19, 2026
# Start: 10:18 PM

# can i sort dictionary in python by value?
#   Yes...
#   Since dictionaries in Python 3.7+ maintain their insertion order, you can pass the sorted results 
#       into the dict() constructor to obtain a new, ordered dictionary.
#   sorted_data_desc = dict(sorted(data.items(), key=lambda item: item[1], reverse=True))

# End: 10:46 PM
# Submission Link: https://leetcode.com/problems/top-k-frequent-elements/submissions/2176313362/
#####################

import unittest

class Solution:    
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        d: dict[int, int] = {}
        for item in nums:
            val = d.get(item)
            if val is None:
                d[item] = 1
            else:
                d[item] = d[item] + 1

        # sort dictionary by value, in desc order
        sorted_d = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        # NOTE: Oct 24 - no need to put them back into a dictionary(?)

        top_k = []
        idx = 1
        for key in sorted_d:
            if idx <= k:
                top_k.append(key)
            else:
                break
            idx = idx + 1

        return top_k
            

        
    

#####################


class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_1(self):
        soln = Solution()
        result = soln.topKFrequent([1,1,1,2,2,3], 2)
        self.assertEqual([1,2], result)

    def test_2(self):
        soln = Solution()
        result = soln.topKFrequent([1], 1)
        self.assertEqual([1], result)

    def test_23(self):
        soln = Solution()
        result = soln.topKFrequent([1,2,1,2,1,2,3,1,3,2], 2)
        self.assertEqual([1,2], result)





if __name__ == '__main__':
  unittest.main()
