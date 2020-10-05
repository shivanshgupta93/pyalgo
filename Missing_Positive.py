####Find the missing positive
'''Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.'''

###Solution:
class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1
        else:
            max_num = max(nums)
            if max_num < 0:
                return 1
            else:
                for i in range(0,max_num+1):
                    if i+1 in nums and i+1 <= max_num:
                        continue
                    elif i+1 not in nums and i+1 <= max_num:
                        return i+1
                    else:
                        return i+1
