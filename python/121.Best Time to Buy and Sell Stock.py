#-*-coding:utf-8-*-
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min_price = 1000000
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            profit = max(profit, prices[i] - min_price)
        return profit
