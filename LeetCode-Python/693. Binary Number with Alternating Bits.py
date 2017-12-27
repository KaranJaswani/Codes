class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        carry = 1 if n % 2 == 0 else 0
        tmp = 0
        
        while n > 1:
            tmp = n % 2
            if tmp ^ carry == 0:
                return False
            else:
                carry = tmp % 2
                n = n / 2

        return bool(tmp ^ 1)

o = Solution()
print(o.hasAlternatingBits(10))
        