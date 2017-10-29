# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        result = []
        self.backtrackPathSum(root, sum, [], result)

    def backtrackPathSum(self, root, sum, lst, result):
        if root == None:
            return

        if sum == root.val and root.left == None and root.right == None:
            lst.append(root.val)
            result.append(list(lst))
            lst.pop(-1)
            return

        lst.append(root.val)
        self.backtrackPathSum(root.left, sum - root.val, lst, result)
        self.backtrackPathSum(root.right, sum - root.val, lst, result)
        lst.pop(-1)


