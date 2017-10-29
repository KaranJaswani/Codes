# Definition for an interval.
import sys


class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

class WrapperIntervalClass(object):
    def __init__(self, interval, index):
        self.interval = interval
        self.index = index

class Solution(object):
    def findRightInterval(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[int]
        """
        result = []
        sortedIntervals = []
        for i in range(0, len(intervals)):
            result.append(-1)
            newInterval = WrapperIntervalClass(intervals[i], i)
            sortedIntervals.append(newInterval)

        sortedIntervals.sort(key= lambda l: l.interval.start)

        for i in range(0, len(intervals)):
            result[i] = self.searchInterval(intervals[i], sortedIntervals)

        return result


    def searchInterval(self, interval, intervals):
        start = 0
        end = len(intervals) - 1
        result = sys.maxint

        while start <= end:
            mid = (start + end) / 2
            if intervals[mid].start >= interval.end:
                result =  min(result, intervals[mid].index)
                end = mid - 1
            elif interval.start < intervals[mid].end: start = mid + 1

        return result

