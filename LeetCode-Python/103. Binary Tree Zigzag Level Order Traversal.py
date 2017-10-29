# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
            return []

        previousLevel = 1
        nextLevel = 0
        queue = [root]
        result = []
        lst = []
        i = 0

        while (previousLevel > 0):
            node = queue.pop(0)
            lst.append(node.val)
            previousLevel -= 1

            if node.left != None:
                queue.append(node.left)
                nextLevel += 1

            if node.right != None:
                queue.append(node.right)
                nextLevel += 1

            if previousLevel == 0:
                if i % 2 == 0:
                    result.append(lst)
                else:
                    result.append(list(reversed(lst)))
                lst = []
                previousLevel = nextLevel
                nextLevel = 0
                i += 1

        return result