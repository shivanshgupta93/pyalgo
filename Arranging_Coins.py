### Arranging Coins
'''
You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.
 

Constraints:

1 <= n <= 231 - 1
'''

##Solution:

class Solution:
    def arrangeCoins(self, n: int) -> int:
        ###Runtime : 1152ms
        '''count = 0
        i = 1
        
        while i <= n:
            n -= i
            count += 1
            i += 1
            
        return count'''
        
        ### Runtime: 28 ms
        left = 1
        right = n
        
        while left <= right:
            mid = int((left + right) / 2)
            
            sum = int((mid*(mid+1))/2)
            
            if sum < n:
                left = mid + 1
            elif sum > n:
                right = mid - 1
            else:
                return mid
            
        return right
        