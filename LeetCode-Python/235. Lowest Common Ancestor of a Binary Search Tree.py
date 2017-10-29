# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root.val >= p and root <= q:
            return root
        elif root.val > p:
            self.lowestCommonAncestor(root.left, p, q)
        else:
            self.lowestCommonAncestor(root.right, p, q)