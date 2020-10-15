###Replace Elements with Greatest Element on Right Side
'''Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

After doing so, return the array.

 

Example 1:

Input: arr = [17,18,5,4,6,1]
Output: [18,6,6,6,1,-1]
 

Constraints:

1 <= arr.length <= 10^4
1 <= arr[i] <= 10^5'''

###Solution:
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        maximum = -1
        result = [0] * len(arr)
        
        for i in range(len(arr)-1,-1,-1):
            result[i] = maximum
            if maximum < arr[i]:
                maximum = arr[i]
                
        return result
                
        