### Excel Sheet Column Number
'''
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
 

Constraints:

1 <= columnTitle.length <= 7
columnTitle consists only of uppercase English letters.
columnTitle is in the range ["A", "FXSHRXW"].

'''

###Solution:
 class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        alpha_dict = dict((y, x+1) for x, y in enumerate(string.ascii_uppercase))

        
        for alpha in columnTitle:
            column_number = (column_number*26) + alpha_dict[alpha]
            
        return column_number
            
        