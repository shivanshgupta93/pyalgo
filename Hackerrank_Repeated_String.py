### Repeated String (Hackerrank)
'''Lilah has a string, , of lowercase English letters that she repeated infinitely many times.

Given an integer, , find and print the number of letter a's in the first  letters of Lilah's infinite string.

For example, if the string  and , the substring we consider is , the first  characters of her infinite string. There are  occurrences of a in the substring.

Function Description

Complete the repeatedString function in the editor below. It should return an integer representing the number of occurrences of a in the prefix of length  in the infinitely repeating string.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Input Format

The first line contains a single string, .
The second line contains an integer, .

Constraints

For  of the test cases, .
Output Format

Print a single integer denoting the number of letter a's in the first  letters of the infinite string created by repeating  infinitely many times.

Sample Input 0

aba
10
Sample Output 0

7
Explanation 0
The first  letters of the infinite string are abaabaabaa. Because there are  a's, we print  on a new line.

Sample Input 1

a
1000000000000
Sample Output 1

1000000000000
Explanation 1
Because all of the first  letters of the infinite string are a, we print  on a new line.'''

###Solution:

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    length_string = len(s)
    full_sub = int(n/length_string)
    count_of_a = s.count('a')
    ###print(full_sub)
    ###print(count_of_a)

    if count_of_a > 0:
        if full_sub == n:
            return n
        elif full_sub < n:
            left_sub = n - (full_sub * length_string)
            ###print(left_sub)
            ###print(s[:left_sub])
            return ((full_sub*count_of_a) + s[:left_sub].count('a'))
    else:
        return 0

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
