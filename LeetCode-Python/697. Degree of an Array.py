class Contents(object):
    def __init__(self, count, start, end):
        self.count = count
        self.start = start
        self.end = end


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        countHash = {}
        for i in range(0, len(nums)):
            num = nums[i]
            if num in countHash:
                countHash[num].count += 1
                countHash[num].end = i
            else:
                countHash[num] = Contents(1, i, i)

        maxCount = 0
        minSubArrayLength = len(nums)
        for key in countHash:
            if countHash[key].count == maxCount:
                subArrayLength = countHash[key].end - countHash[key].start + 1
                if subArrayLength < minSubArrayLength:
                    maxCount = countHash[key].count
                    minSubArrayLength = subArrayLength
            elif countHash[key].count > maxCount:
                subArrayLength = countHash[key].end - countHash[key].start + 1
                maxCount = countHash[key].count
                minSubArrayLength = subArrayLength

        return minSubArrayLength


obj = Solution()
obj.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
