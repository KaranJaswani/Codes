# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True

        previousLevel = 1
        nextLevel = 0
        queue = [root]
        lst = []
        checkQueue = True

        while (previousLevel > 0):
            if checkQueue:
                checkQueue = False
                if not self.isMirror(queue):
                    return False

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
                lst = []
                previousLevel = nextLevel
                nextLevel = 0
                checkQueue = True

        return True

    def isMirror(self, queue):
        i = 0
        j = len(queue) - 1
        while i <= j:
            if ((queue[i].left == None and queue[j].right == None) or
                    (queue[i].left != None and queue[j].right != None and queue[i].left.val == queue[j].right.val)) \
                    and ((queue[i].right == None and queue[j].left == None) or
                             (queue[i].right != None and queue[j].left != None and queue[i].right.val == queue[j].left.val)):
                i += 1
                j -= 1
            else:
                return False

        return True


class Solution(object):
    def isSymmetric(self, root):
        return root == None or self.backtrackIsSymmetric(root.left, root.right)

    def backtrackIsSymmetric(self, left, right):
        if left == None or right == None:
            return left == right

        if left.val != right.val:
            return False

        return self.backtrackIsSymmetric(left.left, right.right) and self.backtrackIsSymmetric(left.right, right.left)
