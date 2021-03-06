# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        
        stack = []

        while len(stack) != 0 or root != None:
            if root == None:
                root = stack.pop()
                k -= 1
                if k == 0:
                    return root.val
                root = root.right

            else:
                stack.append(root)
                root = root.left

        return None
