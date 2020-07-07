# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if not head or not head.next or not head.next.next: return
        
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        pre, cur = None, slow.next
        slow.next = None
        
        while cur:
            n_node = cur.next
            cur.next = pre
            pre = cur
            cur = n_node
            
        while head and pre:
            n_head, n_pre = head.next, pre.next
            head.next = pre
            pre.next = n_head
            head, pre = n_head, n_pre
            
        
