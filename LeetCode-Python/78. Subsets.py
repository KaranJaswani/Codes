class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtracksubsets(nums, 0, result, [])
        return result

    def backtracksubsets(self, nums, k, result, lst):

        result.append(list(lst))

        for i in range(k, len(nums)):
            lst.append(nums[i])
            self.backtracksubsets(nums, i + 1, result, lst)
            lst.pop(-1)


