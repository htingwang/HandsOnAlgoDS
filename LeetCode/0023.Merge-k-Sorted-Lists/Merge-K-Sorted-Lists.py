# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return None
        minheap = []
        
        for l in lists:
            if l:
                heapq.heappush(minheap, (l.val, l))
        
        dummy = ListNode(-1)
        node = dummy
        
        while minheap:
            val, cur = heapq.heappop(minheap)
            node.next = cur
            if cur.next:
                heapq.heappush(minheap, (cur.next.val, cur.next))
            node = node.next
            
        return dummy.next
