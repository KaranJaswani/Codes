import sys 

class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = [-sys.maxint - 1] + nums
        found = False
        prev = nums[0]
        for i in range(1, len(nums) - 1):
            if not (nums[i] <= nums[i + 1]):
                if found: return False
                found = True

                if nums[i + 1] <= prev and i + 1 != len(nums) - 1:
                    return False

            else:
                if i == 1 or nums[i] != nums[i + 1]:
                    prev = nums[i]

        return True
        

o = Solution()
print(o.checkPossibility([1, 2, 4, 5, 3]))