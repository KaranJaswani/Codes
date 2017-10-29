# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        stack = []
        result = []
        while(len(stack) != 0 and root != None):
            if (root == None):
                result.append(stack.pop())
                root = root.right
            else:
                stack.append(root.val)
                root = root.left

        return result

