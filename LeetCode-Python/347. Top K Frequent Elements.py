class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        hash = {}
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
        hash = sorted(hash.items(), key = lambda l : -l[1])

        result = 0
        for i in range(0, k):
            result.append(hash[i])

        return result

obj = Solution()
obj.topKFrequent([1,1,1,1,2,3,1,5,2,3], 4)