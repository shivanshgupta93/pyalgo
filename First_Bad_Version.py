### First Bad Version
'''
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

 

Example 1:

Input: n = 5, bad = 4
Output: 4
Explanation:
call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true
Then 4 is the first bad version.
Example 2:

Input: n = 1, bad = 1
Output: 1
 

Constraints:

1 <= bad <= n <= 231 - 1
'''

##Solution:

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    '''def findBadVersion(self, start, end):
        if end == 1:
            return [1]
        elif start < end:
            print(start,end)
            lst = []
            half = 0
            if int((start + end)/2)%2 == 0:
                half = int((start + end)/2)
            else:
                half = int((start + end)/2) + 1
                
            print(half)

            if isBadVersion(half):
                lst.append(half)
                lst = lst + self.findBadVersion(start,half-1)
                return lst
            elif not isBadVersion(half):
                lst = lst + self.findBadVersion(half+1, end)
                return lst
            
        else:
            return [end+1]'''
        
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        ##lst = self.findBadVersion(0,n)
        ##return min(lst)
        
        start = 0
        end = n
        
        while start <= end:
            print(start,end)
            half = start+(end-start)//2
            print(half)
            if isBadVersion(half):
                end = half - 1
            else:
                start = half + 1
                
        return end + 1
        
     