class Solution(object):
    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.helper(nums, 0, [], result)
        return result

    def helper(self, nums, k, lst, result):
        if len(lst) > 1:
            result.append(list(lst))
        used = [] #Important condition

        for i in range(k, len(nums)):
            if (len(lst) == 0 or nums[i] >= lst[-1]) and nums[i] not in used:
                used.append(nums[i])
                lst.append(nums[i])
                self.helper(nums, i + 1, lst, result)
                lst.pop(-1)
