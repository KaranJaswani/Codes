# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        return self.backtrackSortedListToBST(head, None)

    def backtrackSortedListToBST(self, head, tail):

        if head == tail: return None

        fast = head
        slow = head
        while fast != tail and fast.next != tail:
            fast = fast.next.next
            slow = slow.next

        root = TreeNode(slow.val)
        root.left = self.backtrackSortedListToBST(head, slow)
        root.right = self.backtrackSortedListToBST(slow.next, tail)
        return root

a1 = ListNode(0)
a2 = ListNode(3)
a1.next = a2
obj = Solution()
obj.sortedListToBST(a1)