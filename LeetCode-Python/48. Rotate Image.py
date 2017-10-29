class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        i = 0
        n = len(matrix) - 1
        while i < len(matrix) / 2:

            k = 0
            while k < n:
                temp = matrix[k + i][i + n]
                matrix[k + i][i + n] = matrix[i][k + i]

                temp2 = matrix[i + n][n + i - k]
                matrix[i + n][n + i - k] = temp
                temp = temp2

                temp2 = matrix[n + i - k][i]
                matrix[n + i - k][i] = temp
                temp = temp2

                matrix[i][k + i] = temp
                k += 1

            i += 1
            n -= 2


        print matrix



obj = Solution()
obj.rotate([[1,2,3,4,5],
            [6,7,8,9,10],
            [11,12,13,14,15],
            [16,17,18,19,20],
            [21,22,23,24,25]])

