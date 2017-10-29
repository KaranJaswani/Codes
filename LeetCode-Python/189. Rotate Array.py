class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 0 or k % len(nums) == 0:
            return

        count = 0

        i = 0
        start = 0
        temp = nums[i]

        while count < len(nums):
            pos = (i + k) % len(nums)
            temp1 = nums[pos]
            nums[pos] = temp
            temp = temp1
            i = pos
            count += 1

            if i == start:
                i += 1
                start += 1
                temp = nums[i]



