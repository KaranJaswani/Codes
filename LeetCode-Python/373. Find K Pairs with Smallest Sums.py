class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[List[int]]
        """
        result = []
        used = [False] * min(len(nums1), len(nums2))
        self.helper(nums1, nums2, 0, 0, k, result, used)
        if k > len(nums1) * len(nums2):
            return result[0:len(result) - 1]
        else:
            return result

    def helper(self, nums1, nums2, i, j, k, result, used):
        if i >= len(nums1) or j >= len(nums2) or k == len(result) or (i == j and used[i]):
            return

        if i == j:
            used[i] = True

        lst = []
        lst.append(nums1[i])
        lst.append(nums2[j])
        result.append(lst)

        if i + 1 < len(nums1) and j + 1 < len(nums2) and nums1[i + 1] < nums2[j + 1]:
            self.helper(nums1, nums2, i + 1, j, k, result, used)
            self.helper(nums1, nums2, i, j + 1, k, result, used)
        else:
            self.helper(nums1, nums2, i, j + 1, k, result, used)
            self.helper(nums1, nums2, i + 1, j, k, result, used)




