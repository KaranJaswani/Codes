# Definition for a binary tree node.
import math


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    count = 0

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        self.backtrackPathSum(root, sum)
        return self.count

    def backtrackPathSum(self, root, sum):
        if root == None:
            return

        if sum == root.val:
            self.count += 1

        self.backtrackPathSum(root.left, sum - root.val)
        self.backtrackPathSum(root.right, sum - root.val)

