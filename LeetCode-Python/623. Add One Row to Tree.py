# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        queue = [root]
        lst = []
        depth = 1

        if d == 1:
            newNode = TreeNode(v)
            newNode.left = root
            return newNode
        
        while len(queue) > 0:
            curr = queue.pop(0)
            if depth == d - 1:
                newNode = TreeNode(v)
                newNode.left = curr.left
                curr.left = newNode
                newNode = TreeNode(v)
                newNode.right = curr.right
                curr.right = newNode 
                
            if curr.left != None:
                lst.append(curr.left)
            if curr.right != None:
                lst.append(curr.right)

            if len(queue) == 0:
                queue = lst
                lst = []
                depth += 1
        
        return root
        