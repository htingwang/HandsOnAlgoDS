# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        start = dummy
        #self.reverse(start.next, start.next.next.next)
        #return dummy.next
        while start.next:
            end = start
            for _ in range(k):   
                end = end.next
                if not end: return dummy.next
            
            #print(start.val, end.val)
            start_next = start.next
            self.reverse(start, end)
            #print(start.val, end.val)
            #break
            start = start_next
            
        return dummy.next

    def reverse(self, start, end):
        pre = end.next
        node = start.next
        while pre != end:
            #print(node.val, pre.val, end.val)
            tmp = node.next
            node.next = pre
            pre = node
            node = tmp
        start.next = end
