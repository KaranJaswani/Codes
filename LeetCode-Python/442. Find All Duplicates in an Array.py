class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in xrange(0, len(nums)):
            if nums[i] == 0:
                continue

            while nums[nums[i] - 1] != 0:
                if nums[i] - 1 == i:
                    nums[i] = 0
                    break
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = 0
                nums[i] = temp

        res = []
        for i in xrange(0, len(nums)):
            if nums[i] != 0:
                res.append(nums[i])

        return res

obj = Solution()
obj.findDuplicates([2,1])
