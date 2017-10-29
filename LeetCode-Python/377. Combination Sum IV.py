# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?

class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        hash = {}
        return self.backtrackCombinationSum4(nums, target, hash)

    def backtrackCombinationSum4(self, nums, target, hash):
        if target in hash.keys():
            return hash[target]

        if target < 0:
            return 0

        if target == 0:
            return 1

        result = 0
        for i in nums:
            hash[target - i] = self.backtrackCombinationSum4(nums, target - i, hash)
            result += hash[target - i]

        return result