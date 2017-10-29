class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        neg = 1

        if x < 0:
            neg = -1
            x *= -1

        result = int(''.join(list(str(x))[::-1]))*neg
        if result < -2147483647 or result > 2147483647:
            return 0
        else:
            return result

obj = Solution()
obj.reverse(-123)