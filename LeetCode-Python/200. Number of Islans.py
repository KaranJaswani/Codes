class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    res += 1
                    self.backtrackHelperToMarkIsland(grid, i, j)
        
        return res
    
    def backtrackHelperToMarkIsland(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]) or grid[i][j] == "0": return
        
        grid[i][j] = "0"
        self.backtrackHelperToMarkIsland(grid, i + 1, j)
        self.backtrackHelperToMarkIsland(grid, i, j + 1)
        self.backtrackHelperToMarkIsland(grid, i - 1, j)
        self.backtrackHelperToMarkIsland(grid, i, j - 1)
                        

obj = Solution()
obj.numIslands(["111",
                "010",
                "111"])
