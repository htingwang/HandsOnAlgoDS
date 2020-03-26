# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head;
        while slow and fast:
            slow = slow.next;
            fast = fast.next;
            if fast: fast = fast.next;
            if slow and slow == fast: 
                print slow.val
                while head and slow:
                    if slow == head: return head;
                    head = head.next;
                    slow = slow.next;
        return None;        
