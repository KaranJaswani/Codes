import sys


class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        a = -sys.maxint - 1
        b = -sys.maxint - 1
        c = -sys.maxint - 1
        negb = 0
        negc = 0
        for num in nums:
            if num >= a:
                c = b
                b = a
                a = num
            elif num >= b:
                c = b
                b = num
            elif num >= c:
                c = num

        for num in nums:
            if num < 0:
                if abs(num) >= abs(negb):
                    negc = negb
                    negb = num
                elif abs(num) >= abs(negc):
                    negc = num

        if negb * negc > b * c:
            return a * negb * negc
        else:
            return a * b * c


obj = Solution()
obj.maximumProduct([-4, -3, -2, -1, 60])
