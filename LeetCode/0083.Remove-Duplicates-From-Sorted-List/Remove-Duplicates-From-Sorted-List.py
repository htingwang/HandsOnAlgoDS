# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        
        while node:
            n_node = node.next
            while n_node and n_node.val == node.val:
                n_node = n_node.next
            node.next = n_node
            node = n_node
        
        
        return head
