'''FizzBuzz|List Comprehenssion

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i if non of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
 

Constraints:

1 <= n <= 104
'''

##Solution:

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        '''lst = []
        
        for i in range(1,n+1):
            if i%3 ==0 and i%5 ==0:
                lst.append("FizzBuzz")
            elif i%3 ==0:
                lst.append("Fizz")
            elif i%5 ==0:
                lst.append("Buzz")
            else:
                lst.append(str(i))
                
        return lst'''
        
        return["FizzBuzz" if i%3==0 and i%5==0 else "Fizz" if i%3==0 else "Buzz" if i%5==0 else str(i) for i in range(1,n+1)]