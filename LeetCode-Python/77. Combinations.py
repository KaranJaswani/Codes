class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        self.helper(1, n + 1, k, [], result)
        return result

    def helper(self, start, end, k, lst, result):
        if end - start < k:
            return

        if k == 0:
            result.append(list(lst))
            return

        for i in range(start, end):
            lst.append(i)
            self.helper(i + 1, end, k - 1, lst, result)
            lst.pop(-1)

