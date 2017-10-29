import sys


class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = [- sys.maxint - 1]
        for l in range(len(nums) - 1, -1, -1):
            if nums[l] < stack[-1]:
                return True
            else:
                while stack and nums[l] > stack[-1]:
                    v = stack.pop()
                stack.append(nums[l])
                stack.append(v)
        return False

obj = Solution()
obj.find132pattern([3,5,0,3,4])
obj.find132pattern([3,4,0,1,2])
obj.find132pattern([8,10,4,6,9])

