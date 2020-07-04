# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        pre, cur = ListNode(-1), head
        pre.next = head
        for _ in range(m - 1): pre, cur = pre.next, cur.next
        for _ in range(n - m):
            n_node = cur.next
            cur.next = n_node.next
            n_node.next = pre.next
            pre.next = n_node
        
        return pre.next if pre.val == -1 else head
        
