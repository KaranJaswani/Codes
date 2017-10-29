class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = 0
        for i in xrange(0, len(nums)):
            for j in xrange(i + 1, len(nums)):
                result += self.findHammingDistance(nums[i]^nums[j])

        return result

    def findHammingDistance(self, num):
        """
        :param num: int
        :return: int
        """
        count = 0
        while num != 0:
            count += num & 1
            num >>= 1

        return count
