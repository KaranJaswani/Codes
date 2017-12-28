# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def helper(node, top):
            if node == None:
                return 0
            temp = node.val
            right = helper(node.right, top)
            node.val = node.val + top + right
            left = helper(node.left, node.val)

            return temp + right + left
        
        helper(root, 0)
        return root
            
obj = Solution()
a = TreeNode(2)
b = TreeNode(0)
c = TreeNode(3)
d = TreeNode(-4)
e = TreeNode(1)
a.left = b
a.right = c
b.left = d
b.right = e
obj.convertBST(a)
        