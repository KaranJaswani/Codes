class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        result = [1]
        for i in xrange(1, rowIndex):
            lst = result
            result = []
            for j in xrange(0, i + 1):
                if j == 0 or j == i:
                    result.append(1)
                else:
                    result.append(lst[j - 1] + lst[j])

        return result