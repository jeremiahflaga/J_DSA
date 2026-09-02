#####################
# Leetcode 49 Group Anagrams
# https://leetcode.com/problems/group-anagrams/description/

# Sept 2, 2026
# Start: 11:05 PM

# 

# End: 11:37 PM (excluding unit tests)
# Submission Link: https://leetcode.com/problems/group-anagrams/submissions/2128618187/
#####################

from typing import List
from typing import Dict
import unittest

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict: Dict[str, List[str]]  = {}
        for s in strs:
            sorted_s = ''.join(sorted(s))
            dict_entry = dict.get(sorted_s)
            if dict_entry is None:
                dict[sorted_s] = []

            dict[sorted_s].append(s)

        # Unpack into a List: Use the iterable unpacking operator (*) for a shorter syntax.
        return [*dict.values()]

        # Problem description says "You can return the answer in any order."

        # dict_keys = [*dict.keys()]
        # output = []
        # for key in sorted(dict_keys):
        #     output.append(dict[key])

        # return output

        
    

#####################


class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_1(self):
        soln = Solution()
        result = soln.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
        # print("result: " ,result)

        # Sort each list inside the list
        result_with_sorted_sublist = [sorted(sub_list) for sub_list in result]

        self.assertIn(["bat"], result_with_sorted_sublist)
        self.assertIn(["nat","tan"], result_with_sorted_sublist)
        self.assertIn(["ate","eat","tea"], result_with_sorted_sublist)

    def test_2_empty(self):
        soln = Solution()
        result = soln.groupAnagrams([""])
        # print("result: " ,result)
        self.assertEqual([[""]], result)

    def test_3(self):
        soln = Solution()
        result = soln.groupAnagrams(["a"])
        # print("result: " ,result)
        self.assertEqual([["a"]], result)





if __name__ == '__main__':
  unittest.main()
