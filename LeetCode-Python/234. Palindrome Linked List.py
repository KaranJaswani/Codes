# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = head
        fast = head

        while fast != None and fast.next != None:
            fast = fast.next.next
            slow = slow.next

        ptr1 = self.reverseList(head, slow)
        if fast == None:
            ptr2 = slow
        else:
            ptr2 = slow.next

        while ptr1 != None and ptr2 != None and ptr1.val == ptr2.val:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1 == None and ptr2 == None



    def reverseList(self, head, tail):

        parent = None
        if head != None:
            child = head.next

        while head != tail:
            head.next = parent
            parent = head
            head = child
            if child != None:
                child = child.next

        return parent

obj = Solution()
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(2)
a5 = ListNode(1)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5

obj.isPalindrome(a1)