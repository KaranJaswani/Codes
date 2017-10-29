class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 1
        while i < len(nums):
            if i == 1:
                nums[i] = max(nums[i - 1], nums[i])
            else:
                nums[i] = max(nums[i - 1], nums[i] + nums[i - 2])
            i += 1

        return nums[i - 1]