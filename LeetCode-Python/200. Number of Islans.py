class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        matrix = []
        for s in grid:
            matrix.append(list(s))

        count = 0
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == '1':
                        count += 1
                        self.backtrackMarkNodesZero(matrix, i , j)
        return count

    def backtrackMarkNodesZero(self, matrix, i , j):
        if i < 0 or j < 0 or i >= len(matrix) or j >= len(matrix[i]) or matrix[i][j] == '0': return

        matrix[i][j] = '0'
        self.backtrackMarkNodesZero(matrix, i + 1,j)
        self.backtrackMarkNodesZero(matrix, i, j + 1)
        self.backtrackMarkNodesZero(matrix, i - 1,j)
        self.backtrackMarkNodesZero(matrix, i, j - 1)



obj = Solution()
obj.numIslands(["111",
                "010",
                "111"])
