class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        matrix = []
        for i in range(0, m):
            lst = []
            for j in range(0, n):
                lst.append(0)
            matrix.append(lst)

        for i in range(0, m):
            matrix[i][n - 1] = 1

        for i in range(0, n):
            matrix[m - 1][i] = 1

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, - 1, -1):
                matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]

        return matrix[0][0]

obj = Solution()
obj.uniquePaths(1,1)



