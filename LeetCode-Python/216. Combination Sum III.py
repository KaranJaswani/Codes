class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        result = []
        lst = []
        self.backtrackHelper(k, n, lst, result, 1)
        return result

    def backtrackHelper(self, k, n, lst, result, i):

        if n < 0:
            return

        if k == len(lst) and n == 0:
            result.append(list(lst))
            return

        for j in xrange(i, 10):
            lst.append(i)
            self.backtrackHelper(k - 1, n - i, lst, result, j)
            lst.pop(-1)



