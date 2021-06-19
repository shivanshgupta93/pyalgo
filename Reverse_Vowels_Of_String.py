### Reverse Vowels Of A String
'''
Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both cases.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 

Constraints:

1 <= s.length <= 3 * 105
s consist of printable ASCII characters.
'''

##Solution:
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
		
        ### To exchange pervious vowel with next vowel
		'''list_s = list(s)
        print(list_s)
        previous = 0
        vowel_count = 0
        
        for i in range(len(list_s)):
            if list_s[i] in vowels:
                if vowel_count == 0:
                    vowel_count += 1
                    previous = i
                    continue
                else:
                    list_s[i], list_s[previous] = list_s[previous], list_s[i]
                    previous = i
                    vowel_count += 1
        
        return ''.join(list_s)'''
		
		### Original Solution
        pos_dic = {}
        value_dic = {}
        iterator = 0
        list_s = list(s)
        
        for key, value in enumerate(s):
            if value in vowels:
                pos_dic[iterator] = key
                value_dic[iterator] = value
                iterator += 1
                
        left = 0
        right = len(value_dic.values())
        
        while left < right:
            value_dic[left], value_dic[right-1] = value_dic[right-1], value_dic[left]
            
            left += 1
            right -= 1
            
        for key, value in value_dic.items():
            list_s[pos_dic[key]] = str(value)
            
        return ''.join(list_s)
            
