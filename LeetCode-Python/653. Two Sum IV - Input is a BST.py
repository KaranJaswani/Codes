# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        queue = list()
        _set = set()
        queue.append(root)

        while len(queue) > 0:
            current = queue.pop(0)
            if (k - current.val) in _set:
                return True
            else:
                _set.add((current.val))

            if current.left is not None:
                queue.append(current.left)

            if current.right is not None:
                queue.append(current.right)

        return False
