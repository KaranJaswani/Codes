class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        
        i = 0
        j = 1
        nums = nums + nums
        while len(res) < len(nums) / 2:
            if nums[j] <= nums[i]:
                j = (j + 1)
                if j % (len(nums) / 2) == i:
                    res.append(-1)
                    i = (i + 1)
                    j = (i + 1)
            else:
                res.append(nums[j])
                i = (i + 1) 
                j = (i + 1)
        
        return res

obj = Solution()
obj.nextGreaterElements([1,2,3,2,1])