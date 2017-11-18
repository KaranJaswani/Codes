class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        low = 0
        high = len(nums)
        
        while low < high:
            mid = (low + high) / 2
            if (mid + 1 >= len(nums) or nums[mid] != nums[mid + 1]) and (mid - 1 < 0 or nums[mid] != nums[mid - 1]):
                return nums[mid]
            elif ((high - low + 1) / 2 % 2 == 0 and nums[mid] == nums[mid + 1]) or ((high - low + 1) / 2 % 2 != 0 and nums[mid] == nums[mid - 1]):
                high = mid
            else:
                low = mid + 1
                
    
            

o = Solution()
print(o.singleNonDuplicate([1,1,2]))