class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n >= result:
            n = n - result
            result += 1

        return result