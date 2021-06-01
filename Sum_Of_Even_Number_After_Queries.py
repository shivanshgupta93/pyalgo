####Sum of Even Numbers After Queries
'''We have an array A of integers, and an array queries of queries.

For the i-th query val = queries[i][0], index = queries[i][1], we add val to A[index].  Then, the answer to the i-th query is the sum of the even values of A.

(Here, the given index = queries[i][1] is a 0-based index, and each query permanently modifies the array A.)

Return the answer to all queries.  Your answer array should have answer[i] as the answer to the i-th query.

 

Example 1:

Input: A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
Output: [8,6,2,4]
Explanation: 
At the beginning, the array is [1,2,3,4].
After adding 1 to A[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to A[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to A[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to A[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.'''

###Solution:
class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        '''result = []
        sum = 0
        is_num_even = False
        is_new_even = False
        
        for i in range(0,len(A)):
            if A[i]%2 == 0:
                sum += A[i]

        for query in queries:
            num = A[query[1]]
            new_num = A[query[1]] + query[0]

            if num%2 == 0:
                is_num_even = True
            else:
                is_num_even = False
            
            if new_num %2 == 0:
                is_new_even = True
            else:
                is_new_even = False
                
            if is_new_even and is_num_even:
                sum = (sum - num) + new_num
            if is_new_even and not is_num_even:
                sum += new_num
            if not is_new_even and is_num_even:
                sum -= num
            result.append(sum)
                
            A[query[1]] = new_num
                
        return result'''
        
        result = []
        even_sum = 0
        old_value = 0
        new_value = 0
        
        for i in range(0,len(A)):
            if A[i]%2 == 0:
                even_sum += A[i]
                
        for query in queries:
            old_val = A[query[1]]
            new_val = A[query[1]] + query[0]
            A[query[1]] = new_val
            if old_val % 2 != 0:
                old_val = 0
                
            if new_val % 2 != 0:
                new_val = 0
                
            even_sum = (even_sum - old_val) + new_val
            
            result.append(even_sum)
            
        return result