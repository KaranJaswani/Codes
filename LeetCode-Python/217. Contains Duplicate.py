class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hash = {}

        for num in nums:
            if num in hash:
                return False
            else:
                hash[num] = 1

        return True
