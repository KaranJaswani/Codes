# Definition for singly-linked list.
import random


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):

    length = 0
    h = None
    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.h = head
        while head != None:
            self.length += 1
            head = head.next

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        num = random.randint(1, self.length)

        head = self.h
        while num != 1:
            head = head.next
            num -= 1

        return head.val





# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()