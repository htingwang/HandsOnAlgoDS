# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        while head:
            n_node = head.next
            cur = dummy
            while cur.next and cur.next.val <= head.val: cur = cur.next
            # insert head after cur: cur -> head -> cur.next
            head.next = cur.next
            cur.next = head
            head = n_node
            
        return dummy.next
        
