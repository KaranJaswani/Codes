# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        queue1 = [root]
        queue2 = []
        res = []
        count = 0
        sum = 0
        while len(queue1) > 0:
            elem = queue1[0]
            queue1 = queue1[1:]
            count += 1
            sum += elem.val

            if elem.left != None:
                queue2.append(elem.left)
            
            if elem.right != None:
                queue2.append(elem.right)
            
            if len(queue1) == 0:
                res.append(float(sum)/float(count))
                queue1 = queue2
                queue2 = []
                count = 0
                sum = 0
        
        return res

                

