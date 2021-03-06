####Find All Numbers Disappeared in an Array
'''Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements of [1, n] inclusive that do not appear in this array.

Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.

Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]'''

###Solution:

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        dis_nums = []
        for num in nums:
            pos = abs(num)-1
            
            if nums[pos] > 0:
                nums[pos] *= -1
            
        for i in range(len(nums)):
            if nums[i] > 0:
                dis_nums.append(i+1)
        
        return(dis_nums)
            