class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid) - 1
        if m < 0:
            return 0

        n = len(grid[m]) - 1

        for i in range(m, -1, -1):
            for j in range(n, -1, -1):
                if i == m and j == n: continue
                elif i == m:
                    grid[i][j] += grid[i][j + 1]
                elif j == n:
                    grid[i][j] += grid[i + 1][j]
                else:
                    grid[i][j] += min(grid[i + 1][j], grid[i][j + 1])

        return grid[0][0]
