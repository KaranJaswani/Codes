# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.backtrackFlatten(root)
        return root

    def backtrackFlatten(self, root):
        """
        :param root: TreeNode
        :return: TreeNode; Last Node of the sequence
        """

        if root == None or (root.left ==None and root.right == None):
            return root

        left = self.backtrackFlatten(root.left)
        right = self.backtrackFlatten(root.right)

        if left != None:
            temp = root.right
            root.right = root.left
            root.left = None
            left.right = temp

        if right != None:
            return right
        else:
            return left

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
# a4 = TreeNode(3)
# a5 = TreeNode(4)
# a6 = TreeNode(6)
# a1.left = a2
# a1.right = a3
# a2.left = a4
# a2.right = a5
# a3.right = a6
a1.left = a2
a2.left = a3

obj = Solution()
obj.flatten(a1)


