# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        i = head
        pi = None

        while i != None:
            j = head
            pj = None
            swapped = False
            while j != i:
                if j.val > i.val:
                    pi.next = i.next
                    if pj != None:
                        pj.next = i
                    else:
                        head = i
                    i.next = j
                    swapped = True
                    break
                else:
                    pj = j
                    j = j.next

            if swapped:
                i = pi.next
            else:
                pi = i
                i = i.next

        return head


obj = Solution()
a1 = ListNode(1)
a2 = ListNode(4)
a3 = ListNode(3)
a1.next = a2
a2.next = a3

obj.insertionSortList(a1)







