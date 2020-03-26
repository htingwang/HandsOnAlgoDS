# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head;
        while node:
            tmpnode = node;
            while node.next and node.val == node.next.val:
                node = node.next;
            node = node.next;
            tmpnode.next = node;
        return head;
        
