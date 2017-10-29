class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in xrange(0, len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        for i in xrange(j, len(nums)):
            nums[i] = 0