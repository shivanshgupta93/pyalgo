## Ransom Note:
'''
Given two stings ransomNote and magazine, return true if ransomNote can be constructed from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true
 

Constraints:

1 <= ransomNote.length, magazine.length <= 105
ransomNote and magazine consist of lowercase English letters.
'''

##Solution:

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for word in ransomNote:
            if word in magazine:
                magazine = magazine.replace(word,'',1)
            else:
                return False
            
        return True