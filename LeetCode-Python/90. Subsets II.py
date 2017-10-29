class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        self.backtrackSubsetsWIthDup(nums, -1, [], result)
        return result

    def backtrackSubsetsWIthDup(self, nums, k, lst, result):
        result.append(list(lst))

        for i in range(k + 1, len(nums)):
            if i == k + 1 or nums[i] != nums[i - 1]:
                lst.append(nums[i])
                self.backtrackSubsetsWIthDup(nums, i, lst, result)
                lst.pop(-1)

obj = Solution()
obj.subsetsWithDup([1,2,2])

