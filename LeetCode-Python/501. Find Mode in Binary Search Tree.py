# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    modes = []
    currCount = 0
    maxCount = 0
    currVal = None

    def findMode(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.inorder(root)
        return self.modes

    def inorder(self, root):
        if root is None:
            return
        self.inorder(root.left)
        self.handleValue(root.val)
        self.inorder(root.right)

    def handleValue(self, val):
        if val != self.currVal:
            self.currVal = val
            self.currCount = 0

        self.currCount += 1

        if self.currCount > self.maxCount:
            self.modes = []
            self.modes.append(self.currVal)
            self.maxCount = self.currCount
        elif self.currCount == self.maxCount:
            self.modes.append(self.currVal)

t1 = TreeNode(1, None, TreeNode(2, None, TreeNode(2, None, None)))
o = Solution()
o.findMode(t1)
