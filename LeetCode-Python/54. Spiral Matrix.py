class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []
        m = len(matrix) - 1
        if m < 0: return result
        n = len(matrix[m]) - 1

        left = 0
        right = n
        below = m
        top = 0

        while left <= right and top <= below:
            k = left
            while k <= right:
                result.append(matrix[top][k])
                k += 1

            k = top + 1
            while k <= below:
                result.append(matrix[k][right])
                k += 1

            k = right - 1
            while k >= left and top != below:
                result.append(matrix[below][k])
                k -= 1

            k = below - 1
            while k > top and left != right:
                result.append(matrix[k][left])
                k -= 1

            left += 1
            right -= 1
            below -= 1
            top += 1

        return result

obj = Solution()
obj.spiralOrder([[ 1, 2, 3 ],[ 4, 5, 6 ],[ 7, 8, 9 ]])
obj.spiralOrder([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])
obj.spiralOrder([[1,2,3,4]])

