# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None


class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        left = self.height(root.left)
        right = self.height(root.right)

        return left - right <= 1 and left - right >= -1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def height(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))
