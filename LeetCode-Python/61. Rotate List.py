# Definition for singly-linked list.
import math


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
            return head

        tail = head
        count = 1

        while tail != None and tail.next != None:
            tail = tail.next
            count += 1

        tail.next = head
        if k >= count:
            k = k % count

        count = count - k
        while count != 1:
            head = head.next
            count -= 1

        result = head.next
        head.next = None
        return result


