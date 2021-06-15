#### Climbing Stairs
'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

##Solution:

class Solution:
    def climbStairs(self, n: int) -> int:
        
        if n == 1:
            return 1
        
        f = 1
        s = 2
        
        i = 3
        
        while(i <= n):
            
            f, s = s, f + s
            
            i += 1
            
        return s
        
        ##return self.climb_Stairs(0,n)
        
        
    '''def climb_Stairs(self, step, goal):
        if step > goal:
            return 0
        
        if step == goal:
            return 1
        
        return self.climb_Stairs(step + 1, goal) + self.climb_Stairs(step + 2, goal)'''
    
    
        