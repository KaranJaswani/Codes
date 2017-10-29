class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.insert(0, 1)
        nums.append(1)
        return self.backtrackMaxCoins(nums, {})

    def backtrackMaxCoins(self, nums, hash):
        if len(nums) <= 2:
            return 0

        if str(nums) in hash:
            return hash[str(nums)]

        res = 1
        for i in range(1, len(nums) - 1):
            temp = nums[i - 1] * nums[i] * nums[i + 1]
            temp2 = nums.pop(i)
            res = max(res, temp + self.backtrackMaxCoins(nums, hash))
            nums.insert(i, temp2)

        hash[str(nums)] = res
        return res

obj = Solution()
obj.maxCoins([3,1,5,8])
