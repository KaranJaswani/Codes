class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        return self.helper(nums, S, 0, {})


    def helper(self, nums, S, i, hash):

        if i == len(nums):
            if S == 0:
                return 1
            else:
                return 0

        key = str(S) + "+" + str(i)

        if key in hash:
            return hash[key]

        result = 0

        result += self.helper(nums, S + nums[i], i + 1, hash)
        result += self.helper(nums, S - nums[i], i + 1, hash)

        hash[key] = result

        return result


obj = Solution()
obj.findTargetSumWays([1,1], 0)