import math


class Solution(object):
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        result = [0]
        i = 1
        maxLevel = i * 2

        while i <= maxLevel and i < num:
            length = len(result)
            for j in xrange(0, length):
                result.append(result[j] + 1)
                i += 1
                if i >= num:
                    break
            maxLevel = i * 2

        return result

obj = Solution()
obj.countBits(5)
