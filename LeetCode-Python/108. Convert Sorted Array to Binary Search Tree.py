# Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        return self.helper(0, len(nums), nums)


    def helper(self, i, j, nums):
        if i < j:
            return None
        mid = (i + j) / 2
        root = TreeNode(nums[mid])
        root.left = self.helper(i, mid, nums)
        root.right = self.helper(mid + 1, j, nums)
        return root
