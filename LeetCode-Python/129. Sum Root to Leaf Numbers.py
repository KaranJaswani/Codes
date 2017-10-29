# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        return self.bacltrackSumNumbers(root.left, root.val) + self.bacltrackSumNumbers(root.right, root.val)


    def bacltrackSumNumbers(self, root, number):
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return number * 10 + root.val

        number = number * 10 + root.val

        return self.bacltrackSumNumbers(root.left, number) + self.bacltrackSumNumbers(root.right, number)
