'''

'''

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        profit = 0
        max_profit = 0
        while i < len(prices):
            profit = max(0, profit)
            if i > 0:
                profit += (prices[i] - prices[i-1])
            max_profit = max(max_profit, profit)
            i += 1
        return max_profit

'''
Test Cases
----------
 prices = [10 8 12 14 6]


 Time: O(N)
 Space: O(1)
'''  