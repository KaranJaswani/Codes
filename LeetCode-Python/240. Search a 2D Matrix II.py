class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if len(matrix) == 0:
            return False

        i = 0
        j = len(matrix[i]) - 1

        while i >= 0 and j >= 0:
            if target == matrix[i][j]: return True
            elif target > matrix[i][j]: i += 1
            else: j -= 1

        return False
