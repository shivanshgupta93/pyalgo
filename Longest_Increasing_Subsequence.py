###Longest Increasing Subsequence
'''
Given an unsorted array of integers nums, return the length of the longest continuous increasing subsequence (i.e. subarray). The subsequence must be strictly increasing.

A continuous increasing subsequence is defined by two indices l and r (l < r) such that it is [nums[l], nums[l + 1], ..., nums[r - 1], nums[r]] and for each l <= i < r, nums[i] < nums[i + 1].

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 3
Explanation: The longest continuous increasing subsequence is [1,3,5] with length 3.
Even though [1,3,5,7] is an increasing subsequence, it is not continuous as elements 5 and 7 are separated by element
4.
Example 2:

Input: nums = [2,2,2,2,2]
Output: 1
Explanation: The longest continuous increasing subsequence is [2] with length 1. Note that it must be strictly
increasing.
 

Constraints:

1 <= nums.length <= 104
-109 <= nums[i] <= 109
'''

##Solution:

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        sub_seq = 1
        max_sub_seq = 1
        
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                sub_seq += 1
                print(nums[i], nums[i-1], sub_seq)
            else:
                if max_sub_seq < sub_seq:
                    max_sub_seq = sub_seq
                sub_seq = 1
        if max_sub_seq < sub_seq:
            max_sub_seq = sub_seq        
    
        return max_sub_seq