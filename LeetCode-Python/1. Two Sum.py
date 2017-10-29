class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        result = []
        for i in xrange(0, len(nums)):
            if hash.__contains__(target - nums[i]):
                result.append(i)
                result.append(hash[target - nums[i]])
                return result
            else:
                hash[nums[i]] = i

        return result
