class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        i = 0
        while i < len(matrix):
            if k >= len(matrix[i]):
                k -= len(matrix[i])
                i += 1
            else:
                break

        if k == 0:
            return [i - 1][0]

        j = len(matrix[i])
        while j != k:
            j -= 1

        return matrix[i][j]




obj = Solution()
obj.kthSmallest([[1]], 1)