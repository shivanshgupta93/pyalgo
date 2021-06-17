### Move Zeros
'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
'''

##Solution:

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        zero_lst = []
        pos = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_lst.append(i)
            else:
                if len(zero_lst) == 0:
                    continue
                else:
                    pos = min(zero_lst)
                    zero_lst.remove(pos)
                    zero_lst.append(i)
                    nums[pos] = nums[i]
                    nums[i] = 0
        