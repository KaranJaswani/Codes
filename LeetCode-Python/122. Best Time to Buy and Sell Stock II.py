class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i = 0
        j = 1

        profit = 0
        while j < len(prices):
            if prices[j] < prices[j - 1]:
                if prices[j - 1] - prices[i] >= 0:
                    profit += prices[j - 1] - prices[i]
                    i = j
                else:
                    i = j

            j += 1

        return profit
