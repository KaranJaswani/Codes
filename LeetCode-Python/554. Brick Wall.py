class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        maxBricks = 0
        for i in range(0, len(wall)):
            for j in range(1, len(wall[i])):
                wall[i][j] += wall[i][j - 1]
            maxBricks = wall[i][-1]

        _hash = {}
        for i in range(0, len(wall)):
            for j in range(0, len(wall[i])):
                _hash[wall[i][j]] = _hash.get(wall[i][j], 0) + 1
        _hash[maxBricks] = 0

        res = 0
        for key in _hash:
            res = max(res, _hash[key])

        return len(wall) - res


obj = Solution()
obj.leastBricks([[1], [1], [1]])
