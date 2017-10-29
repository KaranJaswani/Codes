# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        start = head
        parentStart = None

        for i in range(1, m):
            parentStart = start
            start = start.next

        end = head
        for i in range(1, n):
            end = end.next

        ptr = start
        parent = parentStart
        child = ptr.next

        while parent != end:
            ptr.next = parent
            parent = ptr
            ptr = child
            if child != None:
                child = child.next

        if parentStart != None:
            parentStart.next = parent

        start.next = ptr

        return head

a = ListNode(3)
b = ListNode(5)
a.next = b

obj = Solution()
obj.reverseBetween(a,1,2)

