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
        stack1 = []
        stack2 = []

        while l1 != None:
            stack1.append(l1.val)
            l1 = l1.next

        while l2 != None:
            stack2.append(l2.val)
            l2 = l2.next

        head = None
        carry = 0
        while len(stack1) != 0 and len(stack2) != 0:
            num1 = stack1.pop()
            num2 = stack2.pop()
            sum = num1 + num2 + carry
            carry = sum / 10
            sum = sum % 10
            newNode = ListNode(sum)
            newNode.next = head
            head = newNode

        while len(stack1) != 0:
            num1 = stack1.pop()
            sum = num1 + carry
            carry = sum / 10
            sum = sum % 10
            newNode = ListNode(sum)
            newNode.next = head
            head = newNode

        while len(stack2) != 0:
            num1 = stack2.pop()
            sum = num1 + carry
            carry = sum / 10
            sum = sum % 10
            newNode = ListNode(sum)
            newNode.next = head
            head = newNode

        if carry != 0:
            newNode = ListNode(carry)
            newNode.next = head
            head = newNode

        return head


# a = ListNode(7)
# b = ListNode(2)
# c = ListNode(4)
# d = ListNode(3)
# a.next = b
# b.next = c
# c.next = d
#
# e = ListNode(5)
# f = ListNode(6)
# g = ListNode(4)
# e.next = f
# f.next = g

a = ListNode(9)
b = ListNode(1)
c = ListNode(6)
a.next = b
b.next = c

e = ListNode(0)

obj = Solution()
obj.addTwoNumbers(a,e)

