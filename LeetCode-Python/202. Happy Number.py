class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        lst = []
        while(True):
            sum = 0
            while(n != 0):
                temp = n % 10
                n = n / 10
                sum += temp * temp
            if sum == 1:
                return True
            elif lst.__contains__(sum):
                return False
            else:
                lst.append(sum)
                n = sum

        return False

