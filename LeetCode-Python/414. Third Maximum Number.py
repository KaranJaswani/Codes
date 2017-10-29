import sys

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = -sys.maxint - 1
        smax = -sys.maxint - 1
        tmax = -sys.maxint - 1

        for i in xrange(0, len(nums)):
            if nums[i] > max:
                tmax = smax
                smax = max
                max = nums[i]
                continue
            elif nums[i] > smax and nums[i] != max:
                tmax = smax
                smax = nums[i]
                continue
            elif nums[i] > tmax and nums[i] != max and nums[i] != smax:
                tmax = nums[i]
                continue

        if tmax == (-sys.maxint - 1):
            return max
        else:
            return tmax

    def thirdMax(self, nums):
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)

obj = Solution()
obj.thirdMax([1,2,2,5,3,5])