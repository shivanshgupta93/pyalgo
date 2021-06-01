##### Find a Unique Character in String
'''
Given a string, find the first non-repeating character in it and return its index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode"
return 2.
'''

#### Solution:

class Solution:
    def firstUniqChar(self, s: str) -> int:
        if s:
            str_lst = list(s)
            i = 0
            count = 0
            new_lst = []

            while(i==0 and i<len(str_lst)):
                alpha = str_lst[i]
                str_lst.remove(alpha)

                if alpha not in str_lst and alpha not in new_lst:
                    return count

                new_lst.append(alpha)
                count += 1

            return -1
        
        else:
            return -1
            
            
        