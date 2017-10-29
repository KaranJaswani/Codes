# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        currentLevel = 1
        nextLevel = 0

        result = []
        queue = []
        if root != None:
            result.append(root.val)
            queue = [root]

        while len(queue) != 0:
            node = queue.pop(0)
            currentLevel -= 1

            if node.left != None:
                queue.append(node.left)
                nextLevel += 1

            if node.right != None:
                queue.append(node.right)
                nextLevel += 1

            if currentLevel == 0:
                currentLevel = nextLevel
                nextLevel = 0
                if len(queue) > 0:
                    result.append(queue[-1].val)

        return result


