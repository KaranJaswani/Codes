import math

import sys


class Solution(object):

    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        hash = {}
        hash[1] = 1
        hash[2] = 2
        hash[3] = 3
        hash[4] = 1

        for i in range(5, n + 1):
            maxNum = int(math.floor(math.sqrt(i)))
            if maxNum*maxNum == i:
                hash[i] = 1
            else:
                res = sys.maxint
                for j in range(maxNum, 0, -1):
                    j = j * j
                    res = min(res, hash[j] + hash[i - j])

                hash[i] = res

        return hash[n]
