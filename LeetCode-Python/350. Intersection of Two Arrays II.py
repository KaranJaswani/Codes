class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hash = {}
        for num in nums1:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        result = []
        for num in nums2:
            if num in hash and hash[num] > 0:
                hash[num] -= 1
                result.append(num)

        return result