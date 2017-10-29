import sys


class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result1 = -sys.maxint - 1
        product = 1
        for i in nums:
            product *= i
            result1 = max(result1, product)
            if product == 0:
                product = 1

        result2 = -sys.maxint - 1
        product = 1
        nums.reverse()
        for i in nums:
            product *= i
            result2 = max(result2, product)
            if product == 0:
                product = 1

        return max(result1, result2)


obj = Solution()
obj.maxProduct([2,3,-2,4])