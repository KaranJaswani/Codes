class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if desiredTotal <= maxChoosableInteger:
            return True

        A = desiredTotal
        B = 0

        i = 1
        j = maxChoosableInteger

        while desiredTotal >=0:
            print "Total = %d, i = %d, j = %d, i + j = %d" % (desiredTotal, i, j, i + j)
            desiredTotal -= (i + j)
            i += 1
            j -= 1





obj = Solution()
obj.canIWin(4,6)
obj.canIWin(4,7)
obj.canIWin(4,8)