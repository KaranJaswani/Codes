
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        ptr1 = head
        ptr2 = head

        while(ptr1 != None and ptr2 != None):
            ptr1 = ptr1.next
            if(ptr2.next != None):
                ptr2 = ptr2.next.next
            else:
                return False

            if(ptr1 == ptr2):
                return True

        return False

