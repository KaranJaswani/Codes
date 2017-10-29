class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = len(nums) - 1
        k = 0

        while k <= j:
            if nums[k] == 0:
                nums[i] = 0
                i += 1
                k += 1
            elif nums[k] == 2:
                temp = nums[j]
                nums[j] = nums[k]
                nums[k] = temp
                j -= 1
            else:
                k += 1

        while i < k:
            nums[i] = 1
            i += 1


obj = Solution()
obj.sortColors([0,1,2,2,1,0])