class Solution(object):
    hash = {}
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.hash[1] = 1
        self.hash[2] = 1
        self.hash[3] = 2

        res = 0

        for i in xrange(1, n):
            left = max(i, self.integerBreak(i))
            right = max(n - i, self.integerBreak(n - i))
            res = max(res, left*right)

        return res

    def backtrackHelper(self, n):
        if n in self.hash.keys():
            return hash[n]

        res = n
        
        for i in xrange(1, n):
            left = max(i, self.integerBreak(i))
            right = max(n - i, self.integerBreak(n - i))
            res = max(res, left * right)

        return res

