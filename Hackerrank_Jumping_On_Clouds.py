#### Jumping on the Clouds (Hackerrank)
'''Emma is playing a new mobile game that starts with consecutively numbered clouds. Some of the clouds are thunderheads and others are cumulus. She can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus  or . She must avoid the thunderheads. Determine the minimum number of jumps it will take Emma to jump from her starting postion to the last cloud. It is always possible to win the game.

For each game, Emma will get an array of clouds numbered  if they are safe or  if they must be avoided. For example,  indexed from . The number on each cloud is its index in the list so she must avoid the clouds at indexes  and . She could follow the following two paths:  or . The first path takes  jumps while the second takes .

Function Description

Complete the jumpingOnClouds function in the editor below. It should return the minimum number of jumps required, as an integer.

jumpingOnClouds has the following parameter(s):

c: an array of binary integers
Input Format

The first line contains an integer , the total number of clouds. The second line contains  space-separated binary integers describing clouds  where .

Constraints

Output Format

Print the minimum number of jumps needed to win the game.

Sample Input 0

7
0 0 1 0 0 1 0
Sample Output 0

4
Explanation 0:
Emma must avoid  and . She can win the game with a minimum of  jumps:

Sample Input 1

6
0 0 0 0 1 0
Sample Output 1

3
Explanation 1:
The only thundercloud to avoid is . Emma can win the game in  jumps:'''

#### Solution:
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    print(c)
    steps = 0
    if 1 in c:
        pos_not_safe = c.index(1)
        if pos_not_safe <= 1:
            steps += 1
            steps += jumpingOnClouds(c[pos_not_safe+1:])
        else:
            safe_count = c[:pos_not_safe].count(0)
            if (safe_count%2) == 0:
                steps += int(safe_count/2)
                steps += 1
                steps += jumpingOnClouds(c[pos_not_safe+1:])
            else:
                steps += int(safe_count/2)
                steps += 1
                steps += jumpingOnClouds(c[pos_not_safe+1:])
    else:
        safe_count = c.count(0)
        if (safe_count%2) == 0:
            steps += int(safe_count/2)
        else:
            steps += int(safe_count/2)

    return steps



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
