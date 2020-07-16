# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        if fast: slow = slow.next # odd nodes
            
        def reverse(node):
            prev = None
            while node:
                n_node = node.next
                node.next = prev
                prev = node
                node = n_node
            return prev
            
        right = reverse(slow)
        left = head
        while right:
            if left.val != right.val: return False
            right = right.next
            left = left.next
        return True
