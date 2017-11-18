# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

# Track last row and then return first element
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        lastRow = [root]
        leftMost = -1

        while queue:
            curr = queue[0]
            queue = queue[1:]
            lastRow = lastRow[1:]

            if curr.left != None:
                queue.append(curr.left)
                if curr == leftMost:
                    leftMost = curr.left

            if curr.right != None:
                queue.append(curr.right)
                if curr == leftMost:
                    leftMost = curr.right
            
            if not lastRow and queue:
                lastRow = queue
                leftMost = lastRow[0]
        
        return leftMost.val

# Right to left BFS and then return the last node's value
class Solution(object):
    def findBottomLeftValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = [root]
        curr = None

        while queue:
            curr = queue[0]
            queue = queue[1:]

            if curr.right != None:
                queue.append(curr.right)

            if curr.left != None:
                queue.append(curr.left)
            
        return curr.val


o = Solution()
print(o.findBottomLeftValue(TreeNode(1, TreeNode(2, TreeNode(4, None, None), None), TreeNode(3, TreeNode(5, TreeNode(7, None, None), None), TreeNode(6, None, None))))
)