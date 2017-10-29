class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        matrix = []
        for i in range(0, m):
            lst = []
            for j in range(0, n):
                lst.append(0)
            matrix.append(lst)

        for i in range(m - 1, -1, -1):
            if obstacleGrid[i][n - 1] != 1:
                matrix[i][n - 1] = 1

        for i in range(n - 1, -1, -1):
            if obstacleGrid[m - 1][i] != 1:
                matrix[m - 1][i] = 1
                break

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if obstacleGrid[i][j] != 1:
                    matrix[i][j] = matrix[i + 1][j] + matrix[i][j + 1]
                else:
                    matrix[i][j] = 0

        return matrix[0][0]

obj = Solution()
obj.uniquePathsWithObstacles([[0,1]])