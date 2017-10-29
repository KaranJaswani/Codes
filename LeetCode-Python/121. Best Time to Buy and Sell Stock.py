class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        min = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[min]:
                profit = max(profit, prices[i] - prices[min])
            else:
                min = i

        return profit
