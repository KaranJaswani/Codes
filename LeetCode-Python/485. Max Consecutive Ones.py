class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        result = 0
        for i in nums:
            if i == 1:
                count += 1
                result = max(result, count)
            else:
                count = 0

        return result
