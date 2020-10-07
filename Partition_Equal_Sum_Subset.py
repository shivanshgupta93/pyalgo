####Partition Equal Subset Sum
'''Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:

Each of the array element will not exceed 100.
The array size will not exceed 200.
 

Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
 

Example 2:

Input: [1, 2, 3, 5]

Output: false

Explanation: The array cannot be partitioned into equal sum subsets.'''

### Solution:

class Solution:
    def canPartition(self, nums: List[int]) -> bool:   
        if len(nums) >= 2:
            if sum(nums)%2 == 0:
                target = sum(nums)/2
                final_set = set([0,nums[0]])
                for i in range(1,len(nums)):
                    final_set = final_set.union([item+nums[i] for item in final_set])
                    
                if target in final_set:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False