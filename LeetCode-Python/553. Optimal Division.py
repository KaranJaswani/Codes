class Solution(object):
    def optimalDivision(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = map(str, nums)
        return '/'.join(nums) if len(nums) <= 2 else str(nums[0]) + "/(" + "/".join(nums[1:]) + ")"
        