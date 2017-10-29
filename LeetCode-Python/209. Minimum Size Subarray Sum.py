import sys


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        j = 0
        count = 0
        res = sys.maxint

        while i < len(nums) and j < len(nums):
            s -= nums[j]
            count += 1

            if s <= 0:
                res = min(res, count)

            if s < 0:
                while s < 0:
                    s += nums[i]
                    i += 1
                    count -= 1
                res = min(res, count)
                j += 1
            else:
                if j < len(nums):
                    j += 1
                else:
                    break

        if res == sys.maxint: return 0
        else: return res

obj = Solution()
obj.minSubArrayLen(7, [2,3,1,2,4,3])
