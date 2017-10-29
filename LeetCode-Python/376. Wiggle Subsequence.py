class Solution(object):
    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)

        res = 1
        lastDifference = False
        lastNumber = nums[1]
        start = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[0]:
                res += 1
                if nums[i] - nums[0] > 0:
                    lastDifference = True
                lastNumber = nums[i]
                start = i + 1
                break

        for i in range(start, len(nums)):
            if lastDifference:
                if nums[i] - lastNumber >= 0:
                    lastNumber = max(nums[i], lastNumber)
                else:
                    res += 1
                    lastDifference = False
                    lastNumber = nums[i]
            else:
                if nums[i] - lastNumber <= 0:
                    lastNumber = min(nums[i], lastNumber)
                else:
                    res += 1
                    lastDifference = True
                    lastNumber = nums[i]

        return res

obj = Solution()
obj.wiggleMaxLength([33,53,12,64,50,41,45,21,97,35,47,92,39,0,93,55,40,46,69,42,6,95,51,68,72,9,32,84,34,64,6,2,26,98,3,43,30,60,3,68,82,9,97,19,27,98,99,4,30,96,37,9,78,43,64,4,65,30,84,90,87,64,18,50,60,1,40,32,48,50,76,100,57,29,63,53,46,57,93,98,42,80,82,9,41,55,69,84,82,79,30,79,18,97,67,23,52,38,74,15])