### Shift 2D Grid
'''Given a 2D grid of size m x n and an integer k. You need to shift the grid k times.

In one shift operation:

Element at grid[i][j] moves to grid[i][j + 1].
Element at grid[i][n - 1] moves to grid[i + 1][0].
Element at grid[m - 1][n - 1] moves to grid[0][0].
Return the 2D grid after applying shift operation k times.

 

Example 1:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1
Output: [[9,1,2],[3,4,5],[6,7,8]]
Example 2:


Input: grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4
Output: [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]
Example 3:

Input: grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9
Output: [[1,2,3],[4,5,6],[7,8,9]]
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 50
1 <= n <= 50
-1000 <= grid[i][j] <= 1000
0 <= k <= 100'''

###Solution:
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        values_lst = []
        final_grid =[]
        row = []
        no_of_columns = len(grid[0])
        no_of_rows = len(grid)
        for i in range(0,no_of_rows):
            for j in range(0,no_of_columns):
                values_lst.append(grid[i][j])
        
        print(values_lst)
        if k > len(values_lst):
            shift = k%len(values_lst)
        else:
            shift = k
        values_lst = values_lst[len(values_lst)-shift:]+ values_lst[:len(values_lst)-shift]
        print(values_lst)
        
        for value in values_lst:
            row.append(value)
            if len(row) == no_of_columns:
                final_grid.append(row)
                row = []
                
        return final_grid
            