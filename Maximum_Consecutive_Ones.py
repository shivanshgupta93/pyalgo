###Maximum Consecutive Ones:
'''
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
Example 2:

Input: nums = [1,0,1,1,0,1]
Output: 2
 

Constraints:

1 <= nums.length <= 105
nums[i] is either 0 or 1.
'''

##Solution:

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_ones = 0
        length = len(nums)
        
        for i in range(length):
            if nums[i] == 1:
                count += 1
            if nums[i] == 0 or i == length-1:
                if max_ones < count:
                    max_ones = count
                    count = 0
                else:
                    count = 0
                    
        return max_ones