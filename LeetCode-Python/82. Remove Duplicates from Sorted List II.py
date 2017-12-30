# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prevPrev = None
        prev = head
        if prev == None:
            return head
        curr = prev.next

        while curr != None:
            if curr.val == prev.val:
                curr = curr.next
            else:
                if prev.next != curr:
                    if prevPrev != None:
                        prevPrev.next = curr
                    else:
                        head = curr
                else:
                    prevPrev = prev
                prev = curr
                curr = curr.next
        
        if prev.next != curr:
            if prevPrev != None:
                prevPrev.next = curr
            else:
                head = curr
        
        return head
