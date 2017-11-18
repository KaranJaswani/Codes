class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sums = {0:1} # prefix sum array
        res = s = 0
        for n in nums:
            s += n # increment current sum
            res += sums.get(s - k, 0) # check if there is a prefix subarray we can take out to reach k
            sums[s] = sums.get(s, 0) + 1 # add current sum to sum count
        return res
        
obj = Solution()
obj.subarraySum([1,2,3,4,3,5,6,7,8], 8)