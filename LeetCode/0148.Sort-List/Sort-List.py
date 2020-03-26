# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next: return head
        slow, fast, last = head, head, head
        while fast and fast.next:
            last = slow
            slow = slow.next
            fast = fast.next.next
        last.next = None
        #print("#", head, slow)
        return self.merge(self.sortList(head), self.sortList(slow))
    
    def merge(self, l1, l2):
        if not l1: return l2
        if not l2: return l1
        #print(l1.val, l2.val)
        if l1.val < l2.val:
            l1.next = self.merge(l1.next, l2)
            return l1
        else:
            l2.next = self.merge(l1, l2.next)
            return l2
