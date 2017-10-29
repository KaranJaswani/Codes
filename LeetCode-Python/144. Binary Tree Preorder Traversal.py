# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        while len(stack) != 0 or root != None:
            if root == None:
                root = stack.pop()
                root = root.right
            else:
                result.append(root.val)
                stack.append(root)
                root = root.left

        return result
