####Element Appearing More Than 25% In Sorted Array
'''Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time.

Return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
 

Constraints:

1 <= arr.length <= 10^4
0 <= arr[i] <= 10^5'''

###Solution:
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        length = len(arr)
        counter = Counter(arr)
        
        for key, value in counter.items():
            if float(value/length) > 0.25:
                return key
            
