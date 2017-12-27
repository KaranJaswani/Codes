class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        start = 0
        prev_end = 0
        overlap = 0
        res = 0

        for i in range(0, len(timeSeries)):
            start = timeSeries[i]
            if i > 0 and prev_end - start + 1 > 0:
                overlap = prev_end - start + 1
            else:
                overlap = 0
            
            prev_end = start + duration - 1
            res += duration - overlap

        return res

obj = Solution()
obj.findPoisonedDuration([1,2], 2)
