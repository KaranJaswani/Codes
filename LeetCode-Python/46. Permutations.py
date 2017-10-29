class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtrackhelper(nums,[], result)
        return result

    def backtrackhelper(self, nums, lst, result):
        if len(lst) == len(nums):
            result.append(list(lst))
            return

        for i in nums:
            if i not in lst:
                lst.append(i)
                self.backtrackhelper(nums, lst, result)
                lst.pop(-1)



