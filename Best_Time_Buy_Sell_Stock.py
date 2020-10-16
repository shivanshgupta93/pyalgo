#####Best Time to Buy and Sell Stock
'''Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.'''

###Solution:

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''max_profit = 0
        max_price = 0
        for i in range(0,len(prices)):
            max_price = max(prices[i:])
            if (max_price - prices[i]) >= 0:
                if max_profit < (max_price - prices[i]):
                    max_profit = (max_price - prices[i])
                        
        return max_profit'''
        
        
        max_profit = 0
        
        if len(prices) > 0:
            price = prices[0]

            for i in range(1,len(prices)):

                if price >= prices[i]:
                    price = prices[i]

                if max_profit < (prices[i]-price):
                    max_profit = prices[i] - price

            return max_profit
        
        else:
            return 0
            