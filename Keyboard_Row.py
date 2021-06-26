##Keyboard Row
'''
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]
 

Constraints:

1 <= words.length <= 20
1 <= words[i].length <= 100
words[i] consists of English letters (both lowercase and uppercase). 
'''

##Solution:
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        
        word = ''
        picked_row = 0
        keyboard = {1:'qwertyuiopQWERTYUIOP', 2:'asdfghjklASDFGHJKL', 3:'zxcvbnmZXCVBNM'}
        i = 0
        j = 0
        total_words = len(words)
        len_word =  0
        ans = []
        
        while i < total_words:
            if word == words[i]:
                pass
            else:
                word = words[i]
                j = 0
                picked_row = 0
                len_word = len(word)
                ##print(word)
                
            if j == 0:
                if word[j] in keyboard[1]:
                    picked_row = 1
                    j += 1
                    continue
                elif word[j] in keyboard[2]:
                    picked_row = 2
                    j += 1
                    continue
                else:
                    picked_row = 3
                    j += 1
                    continue
                    
            else:
                if j < len_word:
                    if word[j] in keyboard[picked_row]:
                        ##print(word[j])
                        j += 1
                        continue
                    elif word[j] not in keyboard[picked_row]:
                        i += 1
                        ##print(i)
                        continue
                else:
                    i += 1
                    ans.append(word)
                    ##print(ans)
                    continue
                    
        return ans
                    
                
        