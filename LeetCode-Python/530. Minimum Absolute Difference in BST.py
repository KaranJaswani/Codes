# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return min(self.helper(root.left, root.val, root.val), self.helper(root.right, root.val, root.val))
        
    def helper(self, root, maxi, mini):
        if root == None:
            return sys.maxint
        
        lt = self.helper(root.left, root.val, min(root.val, mini))
        rt = self.helper(root.right, max(root.val, maxi), root.val)
        
        return min(min(min(abs(root.val - maxi), abs(root.val - mini)), lt), rt)
        
        