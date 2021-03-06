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
        previous = None
        result = head

        while head != None:
            if previous == None or head.val != previous.val:
                previous = head
                head = head.next
            else:
                previous.next = head.next
                head = head.next

        return result



