class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        isFirstRowZero = False
        isFirstColumnZero = False

        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[i])):
                if matrix[i][j] == 0:
                    if i == 0 and j == 0:
                        isFirstColumnZero = True
                        isFirstRowZero = True
                    elif i == 0:
                        isFirstRowZero = True
                    elif j == 0:
                        isFirstColumnZero = True
                    else:
                        matrix[i][0] = 0
                        matrix[0][j] = 0


        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(0, matrix[i]):
                    matrix[i][j] = 0


        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(0, len(matrix)):
                    matrix[j][i] = 0

        if isFirstRowZero:
            for i in range(0, len(matrix[0])):
                matrix[0][i] = 0

        if isFirstColumnZero:
            for i in range(0, len(matrix)):
                matrix[i][0] = 0

obj = Solution()
obj.setZeroes([[0,0,0,5],[4,3,1,4],[0,1,1,4],[1,2,1,3],[0,0,1,1]])
