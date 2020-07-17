# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next or not head.next.next: return head
        
        pre = head
        node = head.next
        while node and node.next:
            # odd node
            cur = node.next
            # remove cur 
            node.next = node.next.next 
            # insert cur after pre
            cur.next = pre.next
            pre.next = cur
            
            pre = pre.next
            node = node.next
            
        return head
