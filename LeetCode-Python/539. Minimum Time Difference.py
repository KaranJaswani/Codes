import sys

class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        for i in range(0, len(timePoints)):
            time = timePoints[i].split(":")
            timePoints[i] = int(time[0]) * 60 + int(time[1])

        timePoints = sorted(timePoints)

        res = sys.maxint
        for i in range(1, len(timePoints)):
            res = min(res, (timePoints[i] - timePoints[i - 1]) % (24 * 60))

        res = min(res, (timePoints[0] - timePoints[-1]) % (24 * 60))

        return res


obj = Solution()
obj.findMinDifference(["05:31", "22:08", "00:35"])
