###Can Place Flowers
'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
'''

##Solution:

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True
        else:
            output = False

            flower_spots = len(flowerbed)

            flowerbed = [0] + flowerbed + [0]

            for i in range(1,flower_spots+1):
                ##print(i)
                if flowerbed[i] == 0:
                    if flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        n -= 1
                        ##print(flowerbed, n)
                    elif flowerbed[i-1] == 1 or flowerbed[i+1] == 1:
                        continue
                elif flowerbed[i] == 1:
                    continue

                if n == 0:
                    return True

            return False
            
        