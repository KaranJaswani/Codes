# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def helper(node, _str, res):
            if node == None:
                return
            if node.left == None and node.right == None:
                _str = _str + "->" + str(node.val)
                res.append(_str)
                return
            else:
                helper(node.left, _str + "->" + str(node.val), res)
                helper(node.right, _str + "->" + str(node.val), res)

        res = []
        if root == None:
            return res
        _str = str(root.val)
        if root.left == None and root.right == None:
            res.append(_str)
            return res

        helper(root.left, _str, res)
        helper(root.right, _str, res)
        return res
