class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        x = m
        y = n
        for lst in ops:
            x = min(x, lst[0])
            y = min(y, lst[1])

        return x * y


obj = Solution()
obj.maxCount(3, 3, [[2, 2], [3, 3]])
