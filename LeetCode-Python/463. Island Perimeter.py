class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i in xrange(0, len(grid)):
            for j in xrange(0, len(grid[i])):
                if grid[i][j] == 1:
                    if i - 1 < 0 or grid[i - 1][j] == 0:
                        perimeter += 1
                    elif i + 1 >= len(grid) or grid[i + 1][j] == 0:
                        perimeter += 1
                    elif j - 1 < 0 or grid[i][j - 1] == 0:
                        perimeter += 1
                    elif j + 1 >= len(grid[i]) or grid[i][j + 1] == 0:
                        perimeter += 1

        return perimeter


obj = Solution()
obj.islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])