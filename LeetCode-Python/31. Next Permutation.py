class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[i - 1]:
                j = i
                while j < len(nums) and nums[j] >= nums[i - 1]:
                    j += 1

                temp = nums[j - 1]
                nums[j - 1] = nums[i - 1]
                nums[i - 1] = temp
                nums[i:] = sorted(nums[i:])
                return

        nums.sort()

obj = Solution()
obj.nextPermutation([1,3,2])
