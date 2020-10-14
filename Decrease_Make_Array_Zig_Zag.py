####Decrease Elements To Make Array Zigzag
'''Given an array nums of integers, a move consists of choosing any element and decreasing it by 1.

An array A is a zigzag array if either:

Every even-indexed element is greater than adjacent elements, ie. A[0] > A[1] < A[2] > A[3] < A[4] > ...
OR, every odd-indexed element is greater than adjacent elements, ie. A[0] < A[1] > A[2] < A[3] > A[4] < ...
Return the minimum number of moves to transform the given array nums into a zigzag array.

 

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation: We can decrease 2 to 0 or 3 to 1.
Example 2:

Input: nums = [9,6,1,6,2]
Output: 4
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 1000'''

###Solution:
class Solution:
    def movesToMakeZigzag(self, nums: List[int]) -> int:
        even_moves = 0
        odd_moves = 0
        moves = 0
        left = 0
        right = 0
        
        for i in range(0,len(nums)):
            if (i-1) >= 0:
                left = nums[i-1]
            else:
                left = 1001
            
            if (i+1) < len(nums):
                right = nums[i+1]
            else:
                right = 1001
                
            if i%2 == 0:
                if left >= right:
                    moves = (nums[i] - right) +1
                else:
                    moves = (nums[i] - left) + 1
                    
                if moves < 0:
                    moves = 0
                even_moves += moves
                    
            else:
                if left >= right:
                    moves = (nums[i] - right) +1
                else:
                    moves = (nums[i] - left) + 1
                
                if moves < 0:
                    moves = 0
                odd_moves += moves
                    
        return min(odd_moves, even_moves)
                
                
            
        