####Find Words That Can Be Formed by Characters
'''You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.

 

Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
 

Note:

1 <= words.length <= 1000
1 <= words[i].length, chars.length <= 100
All strings contain lowercase English letters only.'''

###Solution:

class Solution:
    class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ###chars_count = Counter(chars)
        word_length = 0
        final_word_length = 0
        
        for word in words:
            chars_count = Counter(chars)
            word_length = 0
            ###print(chars_count)
            for alpha in word:
                if alpha in chars_count:
                    ###print(alpha)
                    if chars_count[alpha] > 0:
                        chars_count[alpha] -= 1
                        word_length += 1
                        ###print(chars_count)
                        ###print(word_length)
                        
                        if word_length == len(word):
                            final_word_length += word_length
                            ####print(final_word)
                            break
                            
                    else:
                        break
                        
                        
        return final_word_length
                
        