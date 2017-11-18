class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        lt = 0
        rt = len(nums) - 1
        while lt < rt:
            middle = (lt + rt) / 2
            if (middle == 0 or nums[middle] > nums[middle - 1]) and (middle == len(nums) - 1 or nums[middle] > nums[middle] + 1):
                return middle
            elif nums[middle] > nums[middle - 1]:
                    lt = middle
            else:
                rt = middle - 1
        
        return -1

obj = Solution()
obj.findPeakElement([1,2,3, 1])
