class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        low = mid = float('inf')
        print low
        for num in nums:
            if num > mid:
                return True

            if num < low:
                low = num
            elif num < mid:
                mid = num
            else:
                return True

        return False





