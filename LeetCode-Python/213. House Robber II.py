class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]

        return max(self.robHelper(nums, 0, len(nums) - 1), self.robHelper(nums, 1, len(nums)))

    def robHelper(self, nums, start, end):

        arr = list(nums[start:end])

        for i in range(1, end - start):
            if i == 1:
                arr[i] = max(arr[i], arr[i - 1])
            else:
                arr[i] = max(arr[i - 1], arr[i] + arr[i - 2])

        if len(arr) > 0:
            return arr[-1]
        else: return 0

obj = Solution()
obj.rob([1])