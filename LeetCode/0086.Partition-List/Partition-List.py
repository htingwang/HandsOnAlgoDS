# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        return self.partition2(head, x)
    
    def partition2(self, head, x):
        smaller = smaller_h = ListNode(-1)
        larger = larger_h = ListNode(-1)
        
        while head:
            if head.val < x:
                smaller.next = head
                smaller = smaller.next
            else:
                larger.next = head
                larger = larger.next
            head = head.next
            
        larger.next = None
        smaller.next = larger_h.next

        return smaller_h.next
        
    def partition1(self, head, x):
        dummy = ListNode(-1)
        dummy.next = head
        pre = dummy
        while pre.next and pre.next.val < x: pre = pre.next
        cur = pre
        while cur.next:
            if cur.next.val >= x:
                cur = cur.next
            else:
                tmp = cur.next # < x
                cur.next = tmp.next
                tmp.next = pre.next
                pre.next = tmp
                pre = pre.next
        return dummy.next
        
