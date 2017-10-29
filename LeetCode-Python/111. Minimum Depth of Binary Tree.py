# Definition for a binary tree node.
import sys


class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            return self.depth(root)

    def depth(self, root):
        if root == None:
            return sys.maxint

        if root.left == None and root.right == None:
            return 1

        return 1 + min(self.depth(root.left), self.depth(root.right))


