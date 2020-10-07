#### Maximum number of baloons
'''Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1
Example 2:



Input: text = "loonbalxballpoon"
Output: 2
Example 3:

Input: text = "leetcode"
Output: 0
 

Constraints:

1 <= text.length <= 10^4
text consists of lower case English letters only.
'''
##Solution:

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        search = 'balon'
        final_dic = {}
        
        for word in search:
            if word in text:
                if word == 'l' or word == 'o':
                    final_dic[word] = int(text.count(word)/2)
                else:
                    final_dic[word] = text.count(word)
            else:
                final_dic[word] = 0
                
        print(final_dic)
        return min(final_dic.values())
                    
                
        