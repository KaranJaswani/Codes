import math


class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num = num % 9

        while (num / 10 != 0):
            sum = 0
            while (num != 0):
                sum += num % 10
                num = num / 10
            num = sum

        return num
