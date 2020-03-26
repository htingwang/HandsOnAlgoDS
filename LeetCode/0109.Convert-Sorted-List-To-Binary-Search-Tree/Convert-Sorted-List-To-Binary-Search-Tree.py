# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None
        if not head.next: return TreeNode(head.val)
        slow, fast, last = head, head, head
        while fast.next and fast.next.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        #fast = slow.next
        right = slow.next
        last.next = None
        cur = TreeNode(slow.val)
        if slow != head: cur.left = self.sortedListToBST(head)
        cur.right = self.sortedListToBST(right)
        return cur
