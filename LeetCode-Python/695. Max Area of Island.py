class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = 0

        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    res = max(res, self.helper(i, j, grid))
        
        return res

    def helper(self, i, j, grid):
        if i >= 0 and j >= 0 and i < len(grid) and j < len(grid[i]) and grid[i][j] == 1:
            grid[i][j] = 0
            return 1 + self.helper(i + 1, j, grid) + self.helper(i, j + 1, grid) + self.helper(i - 1, j, grid) + self.helper(i, j - 1, grid)
        else:
            return 0