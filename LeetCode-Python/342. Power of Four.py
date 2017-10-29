import math

class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        return (num > 0 and str(math.log(num, 4)).split('.')[1] == '0')
