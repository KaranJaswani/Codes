import sys


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        points = sorted(points, key=lambda (h, k) : (h, k))
        lastEnd = -sys.maxint - 1
        count = 0
        for i in xrange(0, len(points)):
            if points[i][0] <= lastEnd:
                lastEnd = min(lastEnd, points[i][1])
            else:
                count += 1
                lastEnd = points[i][1]

        return count
