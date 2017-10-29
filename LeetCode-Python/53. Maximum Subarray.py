import sys


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum = nums[0]
        for i in xrange(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            maxSum = max(maxSum, nums[i])

        return maxSum


