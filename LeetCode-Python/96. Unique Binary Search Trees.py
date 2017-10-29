class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        hash = {}
        hash[0] = 1
        hash[1] = 1
        hash[2] = 2

        return self.backtrackNumTrees(n, hash)

    def backtrackNumTrees(self, n, hash):
        if n in hash:
            return hash[n]

        res = 0
        for i in range(1, n + 1):
            res += self.backtrackNumTrees(i - 1, hash) * self.backtrackNumTrees(n - i, hash)

        hash[n] = res
        return res