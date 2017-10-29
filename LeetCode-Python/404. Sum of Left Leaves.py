# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root == None):
            return 0

        if (root.left != None):
            return root.left.val + self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.right)

