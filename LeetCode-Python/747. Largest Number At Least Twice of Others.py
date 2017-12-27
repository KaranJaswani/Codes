import sys

class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = -sys.maxint - 1
        secondLargest = -sys.maxint - 1
        for num in nums:
            if num > largest:
                secondLargest = largest
                largest = num
            elif num > secondLargest:
                secondLargest = num

        if secondLargest * 2 <= largest:
            return nums.index(largest)
        else:
            return -1

obj = Solution()
obj.dominantIndex([0,0,0,1])