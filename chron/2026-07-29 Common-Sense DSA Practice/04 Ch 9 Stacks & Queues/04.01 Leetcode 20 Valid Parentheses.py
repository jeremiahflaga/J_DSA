#####################
# Leetcode 20 Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/description/

# Nov 11, 2026
# Start: 9:48 PM

# use dictionary { { ')' : '(' },  { ']' : '[' }, etc}
#   use stack to store each token
#   if next token is a key in the dictionary
#       then peek into the stack to see if the next token has the same value as the value for that dictionary key
#       if they have the same value, return true, if not return false


# End: 10:16 PM (error on first submission, see test 6 below)
# Submission Link: https://leetcode.com/problems/valid-parentheses/submissions/2193929503/

# End: 10:25 PM (solution accepted)
# Submission Link: https://leetcode.com/problems/valid-parentheses/submissions/2193934836/
#####################


from typing import List
from typing import Dict
import unittest
from collections import deque # use deque for stack

class Solution:
    def isValid(self, s: str) -> bool:
        paren_dict = { ')' : '(' ,   ']' : '[' , '}' : '{' }
        stack = deque()

        first_paren = s[0]
        stack.append(first_paren)
        for paren in s[1:]:
            paren_open_equivalent = paren_dict.get(paren)
            if paren_open_equivalent is None:    # this is an open paren or bracket, so append to stack
                stack.append(paren)
            else:                           # close bracket
                # === solution to first error encountered ===
                if len(stack) == 0: # got a close bracket, but stack is empty, so it has no equivalent open bracket
                    return False
                # === end of solution to first error encountered ===
                paren_popped_from_stack = stack.pop()
                if paren_popped_from_stack != paren_open_equivalent:
                    return False

        if len(stack) > 0:
            return False

        return True
           

        
    

#####################


class Tests(unittest.TestCase):
  
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs) 

    def test_1(self):
        soln = Solution()
        result = soln.isValid("()")
        self.assertTrue(result)

    def test_2(self):
        soln = Solution()
        result = soln.isValid("()[]{}")
        self.assertTrue(result)

    def test_3(self):
        soln = Solution()
        result = soln.isValid("(]")
        self.assertFalse(result)

    def test_4(self):
        soln = Solution()
        result = soln.isValid("([])")
        self.assertTrue(result)

    def test_5(self):
        soln = Solution()
        result = soln.isValid("([)]")
        self.assertFalse(result)

    # NOTE: got an error on first submission
    # IndexError: pop from an empty deque
    #     paren_popped_from_stack = stack.pop()
    # Line 15 in isValid (Solution.py)
    #     ret = Solution().isValid(param_1)
    # Line 49 in _driver (Solution.py)
    #     ~~~~~~~^^
    #     _driver()
    # Line 64 in <module> (Solution.py)
    #
    # Last Executed Input: s = "(){}}{"
    def test_6(self):
        soln = Solution()
        result = soln.isValid("(){}}{")
        self.assertFalse(result)






if __name__ == '__main__':
  unittest.main()
