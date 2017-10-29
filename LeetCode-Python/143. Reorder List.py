# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        if head == None or head.next == None:
            return head

        slow = head
        fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        head2 = slow.next
        slow.next = None

        head2 = self.reverseList(head2)
        result = head
        while head2 != None:
            temp1 = head.next
            temp2 = head2.next

            head.next = head2
            head2.next = temp1

            head = temp1
            head2 = temp2


    def reverseList(self, head):
        if head == None:
            return None

        parent = None
        child = head.next

        while head != None:
            head.next = parent
            parent = head
            head = child
            if child != None:
                child = child.next

        return parent

