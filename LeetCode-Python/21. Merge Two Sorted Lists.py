# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        head = l1
        pl1 = None
        while l1 != None and l2 != None:
            if l2.val < l1.val:
                if pl1 == None:
                    temp = l2
                    l2 = l2.next
                    temp.next = l1
                    pl1 = temp
                    head = pl1
                else:
                    temp = l2
                    l2 = l2.next
                    pl1.next = temp
                    temp.next = l1
                    pl1 = temp
            else:
                pl1 = l1
                l1 = l1.next

        if l2 != None:
            if pl1 != None:
                pl1.next = l2
            else:
                head = l2

        return head

