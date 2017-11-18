# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        return self.helper(1, n)
    
    def helper(self, low, high):
        num = (low + high) / 2
        if guess(num) == 0:
            return num
        elif guess(num) == -1:
            return self.helper(low, num)
        else: 
            return self.helper(num + 1, high)
        