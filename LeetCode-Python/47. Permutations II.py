class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        result = []
        visited = [0] * len(nums)
        self.backtrackPermuteUnique(nums, [], result, visited)
        return result

    def backtrackPermuteUnique(self, nums, lst, result, visited):
        if len(nums) == len(lst):
            result.append(list(lst))
            return

        for i in range(0, len(nums)):
            if visited[i] == 0 and (i == 0 or nums[i] != nums[i - 1] or visited[i - 1]):
                visited[i] = 1
                lst.append(nums[i])
                self.backtrackPermuteUnique(nums, lst, result, visited)
                lst.pop(-1)
                visited[i] = 0

obj = Solution()
obj.permuteUnique([1,1,2])