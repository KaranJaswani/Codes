class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        lst = [0]* n
        result = []
        for i in range(0, n):
            result.append(lst)

        m = n - 1
        n = n - 1

        left = 0
        right = n
        below = m
        top = 0
        num = 1

        while left <= right and top <= below:
            k = left
            while k <= right:
                result[top][k] = num
                num += 1
                k += 1

            k = top + 1
            while k <= below:
                result[k][right] = num
                num += 1
                k += 1

            k = right - 1
            while k >= left and top != below:
                result[below][k] = num
                num += 1
                k -= 1

            k = below - 1
            while k > top and left != right:
                result[k][left] = num
                num += 1
                k -= 1

            left += 1
            right -= 1
            below -= 1
            top += 1

        return result

obj = Solution()
obj.generateMatrix(3)