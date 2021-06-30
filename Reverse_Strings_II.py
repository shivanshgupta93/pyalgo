##Reverse String II
'''
Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"
 

Constraints:

1 <= s.length <= 104
s consists of only lowercase English letters.
1 <= k <= 104
'''

##Solution:
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        
        start = 0
        
        len_s = len(s)
        
        pairs = int(len_s/k)
        
        
        output = ''
        
        if len_s == k:
            return s[::-1]
        else:
            for i in range(pairs+1):
                start = i*k
                if i%2 == 0:
                    output += s[start:start+k][::-1]
                else:
                    output += s[start:start+k]
                    
            output += s[start+k:]
            return output
                