## Valid Paranthesis
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

##Solution:
class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s)%2) !=0:
            return False
        else:
            stack = []
            for char in s:
                if char in ['(', '{', '[']:
                    stack.append(char)
                elif len(stack) <= 0:
                    return False
                elif char in [')', '}', ']']:
                    poped = stack.pop()
                    if poped == '{' and char != '}':
                        return False
                    elif poped == '[' and char != ']':
                        return False
                    elif poped == '(' and char != ')':
                        return False
            return len(stack) == 0
                
        