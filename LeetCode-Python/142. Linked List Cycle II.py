# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ptr1 = head
        ptr2 = head
        firstTime = True

        while ptr2 != None and (ptr1.val != ptr2.val or firstTime):
            firstTime = False
            ptr1 = ptr1.next
            ptr2 = ptr2.next

            if ptr2 != None:
                ptr2 = ptr2.next
            else:
                break

        if ptr2 == None:
            return None

        ptr1 = head

        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr2

obj = Solution()
a = ListNode(1)
b = ListNode(2)
a.next = b
b.next = a
obj.detectCycle(a)




