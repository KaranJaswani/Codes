# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda l: (l.start, l.end))
        if len(intervals) > 0:
            previousInterval = intervals[0]
        count = 0

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if previousInterval != None and interval.start < previousInterval.end:
                count += 1
                if interval.end < previousInterval.end:
                    previousInterval = interval #Important Condition
            else:
                previousInterval = interval

        return count




