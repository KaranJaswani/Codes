class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        sortedNums = sorted(
            ((nums[i], i) for i in range(0, len(nums))), key=lambda l: -l[0])
        res = [0] * len(nums)
        for i in range(0, len(sortedNums)):
            if i == 0:
                res[sortedNums[i][1]] = "Gold Medal"
            elif i == 1:
                res[sortedNums[i][1]] = "Silver Medal"
            elif i == 2:
                res[sortedNums[i][1]] = "Bronze Medal"
            else:
                res[sortedNums[i][1]] = str(i + 1)

        return res


obj = Solution()
print(obj.findRelativeRanks([1, 2, 3, 4, 5]))
