class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []

        for i in xrange(0, len(nums)):
            while(nums[i] != 0 and nums[nums[i] - 1] != 0):
                if nums[i] - 1 == i:
                    nums[i] = 0
                    break
                else:
                    temp = nums[nums[i] - 1]
                    nums[nums[i] - 1] = 0
                    nums[i] = temp

        for i in xrange(0, len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result


