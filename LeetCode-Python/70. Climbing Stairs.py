class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        one = 1
        two = 2
        sum = 0
        if n == 1:
            return one
        elif n == 2:
            return two
        else:
            for i in xrange(3, n + 1):
                sum = one + two
                one = two
                two = sum
            return sum


