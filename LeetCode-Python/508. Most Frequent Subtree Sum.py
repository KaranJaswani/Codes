# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left, right):
        self.val = x
        self.left = left
        self.right = right

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        
        lst = {}
        self.helper(root, lst)
        
        max = 0
        res = []
        for key,value in lst.iteritems():
            if value > max:
                res = []
                res.append(key)
                max = value
            elif value == max:
                res.append(key)
        
        return res
    
    def helper(self, node, lst):
        if node == None:
            return 0
        
        val = node.val + self.helper(node.left, lst) + self.helper(node.right, lst)
        
        lst[val] = lst.get(val, 0) + 1
        
        return val

o = Solution()
o.findFrequentTreeSum(TreeNode(5, TreeNode(2, None, None), TreeNode(-5, None, None)))