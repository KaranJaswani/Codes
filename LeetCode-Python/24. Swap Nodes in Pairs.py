# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node1 = None
        node2 = head
        if node2 == None:
            return head
        node3 = node2.next
        if node3 == None:
            return head
        node4 = node3.next
        if node2 == None or node3 == None:
            return head

        while node3 != None:
            if node1 != None:
                node1.next = node3
            else:
                head = node3
            node3.next = node2
            node2.next = node4

            node1 = node2
            node2 = node4
            if node2 != None:
                node3 = node2.next
            else:
                node3 = None
            if node3 != None:
                node4 = node3.next
            else:
                node4 = None

        return head
