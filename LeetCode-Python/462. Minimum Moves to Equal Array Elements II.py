import math


class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # result = 0
        nums.sort()
        median = nums[len(nums) / 2]
        # for i in nums:
        #     result += int(math.fabs(i - median))
        nums[:] = [math.fabs(x - median) for x in nums]

        # return result
        return sum(nums)