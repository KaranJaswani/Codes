# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def getSum(node):
            if node == None:
                return 0

            return node.val + getSum(node.left) + getSum(node.right)
        
        if root == None:
            return 0
        
        left = getSum(root.left)
        right = getSum(root.right)
        return abs(left - right) + self.findTilt(root.left) + self.findTilt(root.right)