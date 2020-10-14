###Check If It is a Straight Line
'''You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

 

 

Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false
 

Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.'''

###Solution:
class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        '''is_straight = False
        difference = coordinates[0][1] - coordinates[0][0]
        for element in coordinates[1:]:
            if difference == (element[1] - element[0]):
                difference = element[1] - element[0]
                is_straight = True
            else:
                is_straight = False
                break
        
        return is_straight
        
        sum_x = 0
        sum_y = 0
        x = 0
        y = 0
        no_of_coordinates = len(coordinates)
        is_straight = False
        diff_dic = {}
        difference = coordinates[0][1] - coordinates[0][0]
        
        for i in range(0,no_of_coordinates):
            if difference == (coordinates[i][1] - coordinates[i][0]):
                diff_dic[i] = 1
                difference = coordinates[i][1] - coordinates[i][0]
            else:
                diff_dic[i] = 0
            sum_x += coordinates[i][0]
            x = max(x,coordinates[i][0])
            sum_y += coordinates[i][1]
            y = max(y,coordinates[i][1])
            
        ##print(no_of_coordinates)
        ##print(sum_x, sum_y)
        ###print(sum(diff_dic.values()))
        if sum_x == 0 or sum_y ==0:
            is_straight = True
        elif (sum_x/no_of_coordinates)/x == 1 or (sum_y/no_of_coordinates)/y ==1:
            is_straight = True
        elif sum(diff_dic.values())%no_of_coordinates ==0:
            is_straight = True
        else:
            is_straight = False
        
        return is_straight'''
        
        is_straight = False
        if len(coordinates) > 2:
            for i in range(1,len(coordinates)-1):
                slope_1 = (coordinates[i+1][0] - coordinates[i][0]) * (coordinates[i][1] - coordinates[i-1][1])
                slope_2 = (coordinates[i+1][1] - coordinates[i][1]) * (coordinates[i][0] - coordinates[i-1][0])
                if slope_1 == slope_2:
                    is_straight = True
                else:
                    is_straight = False
                    break
            
        else:
            is_straight = True
        return is_straight
                
            
            
        