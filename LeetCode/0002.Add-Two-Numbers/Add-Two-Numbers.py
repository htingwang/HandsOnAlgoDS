# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        c = 0
        dummy = ListNode(-1)
        node = dummy
        while l1 or l2:
            s1 = s2 = 0
            if l1: 
                s1 = l1.val
                l1 = l1.next
            if l2:
                s2 = l2.val
                l2 = l2.next
            
            s = s1 + s2 + c
            node.next = ListNode(s % 10)
            node = node.next
            c = s // 10
        if c:
            node.next = ListNode(c)
        return dummy.next
