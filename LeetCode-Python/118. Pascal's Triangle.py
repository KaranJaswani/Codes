class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in xrange(0, numRows):
            lst = []
            for j in xrange(0, i + 1):
                if j == 0 or j == i:
                    lst.append(1)
                else:
                    lst.append(result[len(result) - 1][j - 1] + result[len(result) - 1][j])
            result.append(lst)

        return result
