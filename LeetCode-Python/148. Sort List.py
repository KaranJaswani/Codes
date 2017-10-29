# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        return self.helper(head, None)

    def helper(self, head, tail):
        if head == tail:
            if head != None:
                return ListNode(head.val)
            else:
                return None

        mid = self.FindMid(head, tail)
        left = self.helper(head, mid)
        right = self.helper(mid.next, tail)

        newHead = None
        newTail = None

        while left != None or right != None:
            if left == None:
                newNode = ListNode(right.val)
                right = right.next
            elif right == None or left.val < right.val:
                newNode = ListNode(left.val)
                left = left.next
            else:
                newNode = ListNode(right.val)
                right = right.next

            if newTail == None:
                newHead = newNode
                newTail = newNode
            else:
                newTail.next = newNode
                newTail = newTail.next


        return newHead


    def FindMid(self, head, tail):
        slow = head
        fast = head

        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next

        return slow

obj = Solution()
a1 = ListNode(1)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3
obj.sortList(a1)