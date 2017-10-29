class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False

        nums.sort()
        return self.backtrackCanPartition(nums, len(nums) - 1, totalSum / 2)

    def backtrackCanPartition(self, nums, k, sum):
        if sum == 0:
            return True

        for i in range(k, -1, - 1):
            if sum - nums[i] < 0: break
            if self.backtrackCanPartition(nums, i - 1 , sum - nums[i]): return True

        return False