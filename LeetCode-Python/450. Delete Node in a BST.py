# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if root == None:
            return root

        parentNode = self.FindNode(None, root, key)
        if parentNode == None and root.val != key:
            return root

        node = None
        if parentNode == None:
            node = root
        elif parentNode.left != None and parentNode.left.val == key:
            node = parentNode.left
        else:
            node = parentNode.right

        if node.left == None or node.right == None:
            if node.left == None:
                if parentNode == None:
                    root = node.right
                elif parentNode.left != None and parentNode.left.val == key:
                    parentNode.left = node.right
                else:
                    parentNode.right = node.right
            else:
                if parentNode == None:
                    root = node.left
                elif parentNode.left != None and parentNode.left.val == key:
                    parentNode.left = node.left
                else:
                    parentNode.right = node.left
        else:
            successorNode = self.FindSuccessor(node)
            node.val = successorNode.val
            if successorNode == node.right:
                node.right = successorNode.right
            else:
                self.deleteNode(node.right, successorNode.val)

        return root

    def FindNode(self, parent, root, key):
        if root == None: return None
        if root.val == key:
            return parent
        elif root.val > key:
            return self.FindNode(root, root.left, key)
        else:
            return self.FindNode(root, root.right, key)

    def FindSuccessor(self, root):
        rightNode = root.right
        while rightNode.left != None:
            rightNode = rightNode.left

        return rightNode

obj = Solution()

a1 = TreeNode(2)
a2 = TreeNode(1)
a1.left = a2

# a3 = TreeNode(6)
# a4 = TreeNode(2)
# a5 = TreeNode(4)
# a6 = TreeNode(7)
# a1.left = a2
# a1.right = a3
# a2.left = a4
# a2.right = a6
# a3.right = a6

obj.deleteNode(a1, 1)
