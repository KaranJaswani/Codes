import math


class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        temp = 0
        bits = math.floor(math.log(num, 2))

        while bits >= 0:
            temp += int(math.pow(2, bits))
            bits -= 1

        return num^temp

obj = Solution()
obj.findComplement(3)