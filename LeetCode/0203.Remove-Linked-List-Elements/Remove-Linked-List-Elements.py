# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        node = dummy
        while node and node.next:
            if node.next.val == val:
                node.next = node.next.next
            else: node = node.next
        return dummy.next
                
        
