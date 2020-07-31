'''Array of Doubled Pairs'''
'''Given an array of integers A with even length, return true if and only if it is possible to reorder it such that A[2 * i + 1] = 2 * A[2 * i] for every 0 <= i < len(A) / 2.'''
'''Example 1:

Input: [3,1,3,6]
Output: false
Example 2:

Input: [2,1,2,6]
Output: false
Example 3:

Input: [4,-2,2,-4]
Output: true
Explanation: We can take two groups, [-2,-4] and [2,4] to form [-2,-4,2,4] or [2,4,-2,-4].
Example 4:

Input: [1,2,4,16,8,4]
Output: false
'''

##Solution:
class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        count = Counter(A)
        for num in sorted(A, key=abs):
            if count[num] <= count[2*num]:
                count[2*num] -= count[num]
                count[num] = 0
            else:
                return False
        
        return True
        
        '''if len(A)%2 !=0:
            return False
        else:
            is_bool = 0
            i = 0
            A = sorted(A, key=abs)
            while (A):
                num = A[i]
                if 2*num in A:
                    A.remove(num)
                    if 2*num in A:
                        A.remove(2*num)
                        is_bool = 0
                    else:
                        is_bool = 1
                        break
                else:
                    is_bool = 1
                    break
                    
            if is_bool == 0:
                return True
            else:
                return False'''
                    
        