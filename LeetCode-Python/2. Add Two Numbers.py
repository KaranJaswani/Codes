# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        res = None
        prevNode = None
        while l1 != None or l2 != None or carry != 0:
            if l1 == None and l2 == None and carry != 0:
                _sum = carry
            elif l1 == None:
                _sum = l2.val + carry
            elif l2 == None:
                _sum = l1.val + carry
            else:
                _sum = l1.val + l2.val + carry
            val = _sum % 10
            carry = _sum / 10
            newNode = ListNode(val)
            if res == None:
                res = newNode
                prevNode = newNode
            else:
                prevNode.next = newNode
                prevNode = newNode
            if l1 != None:
                l1 = l1.next
            if l2 != None:
                l2 = l2.next

        return res
