class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stepsNeeded = 0
        i = len(nums) - 1
        while i > 0:
            if nums[i] >= stepsNeeded:
                stepsNeeded = 1
            else:
                stepsNeeded += 1
            i -= 1

        return nums[0] >= stepsNeeded