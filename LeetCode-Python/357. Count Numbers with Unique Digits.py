class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0

        product = 9
        sum = 10

        for i in xrange(2, n + 1):
            product *= 9 - (i - 2)
            sum += product

        return sum

obj = Solution()
obj.countNumbersWithUniqueDigits(3)
