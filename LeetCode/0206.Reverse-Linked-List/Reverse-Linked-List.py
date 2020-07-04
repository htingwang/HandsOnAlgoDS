# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        return self.reverseList2(head)
        
    def reverseList1(self, head):
        if not head or not head.next: return head
        node = self.reverseList1(head.next)
        head.next.next = head
        head.next = None
        return node
    
    def reverseList2(self, head):
        if not head or not head.next: return head
        
        pre = head
        cur = head.next
        pre.next = None
        while cur:
            n_node = cur.next
            cur.next = pre
            pre = cur
            cur = n_node
        return pre
