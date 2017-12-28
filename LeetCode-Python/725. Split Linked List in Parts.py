# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        def getLength(root):
            count = 0
            while root != None:
                count += 1
                root = root.next
            return count
        
        if k == 1:
            return [root]
        
        length = getLength(root)
        rem = length % k
        perfectDiv = int(math.ceil(float(length) / float(k)))

        count = 0
        res = []
        while root != None:
            curr = root
            if count == 0:
                res.append(curr)
            count += 1

            root = root.next
            if rem > 0:
                if count == perfectDiv:
                    count = 0
                    curr.next = None
                    rem -= 1
            else:
                if length % k == 0:
                    if count == perfectDiv: 
                        count = 0
                        curr.next = None
                elif count == perfectDiv - 1:
                        count = 0
                        curr.next = None

        while len(res) != k:
            res.append(None)
            
        return res        