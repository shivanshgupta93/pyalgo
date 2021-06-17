### Word Pattern
'''
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

 

Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true
Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", s = "dog dog dog dog"
Output: false
 

Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lower-case English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
'''

##Solution:

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        list_s = s.split(" ")
        
        if len(pattern) != len(list_s):
            return False
        
        else:
            for i in range(len(pattern)):
                if pattern[i] not in dic:
                    dic[pattern[i]] = list_s[i]
                else:
                    if dic[pattern[i]] != list_s[i]:
                        return False

            return len(set(pattern))==len(set(dic.values()))
            