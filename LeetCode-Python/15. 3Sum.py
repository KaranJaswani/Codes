class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        resultString = []
        nums.sort()
        for i in range(0, len(nums)):
            fixedNumber = nums[i]
            lst = self.twoSum(nums, i + 1, len(nums), -fixedNumber)

            for list in lst:
                s = str(fixedNumber) + str(list[0]) + str(list[1])
                if s not in resultString:
                    resultString.append(s)
                    l = [fixedNumber, list[0], list[1]]
                    result.append(l)

        return result

    def twoSum(self, nums, start, end, target):
        hash = []
        result = []
        for i in range(start, end):
            if (target - nums[i]) in hash:
                lst = []
                lst.append(target - nums[i])
                lst.append(nums[i])
                result.append(lst)

            hash.append(nums[i])

        return result

obj = Solution()
obj.threeSum([-1, 0, 1, 2, -1, -4])




