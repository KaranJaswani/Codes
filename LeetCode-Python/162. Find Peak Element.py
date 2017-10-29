import sys


class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        start = 1
        end = len(nums) - 1

        while start <= end:
            mid = (start + end) / 2
            if (mid - 1 < 0 or nums[mid] > nums[mid - 1]) and (mid + 1 >= len(nums) or nums[mid] > nums[mid + 1]):
                return mid
            elif nums[mid] < nums[mid - 1]:
                end = mid - 1
            else:
                start = mid

        return 0

obj = Solution()
obj.findPeakElement([1,2,3])
