# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = ListNode(0)
        pre.next = head
        none_nine = None
        node = pre
        while node:
            if node.val != 9: none_nine = node
            node = node.next
        none_nine.val += 1
        node = none_nine.next
        while node:
            node.val = 0
            node = node.next
        return pre if pre.val != 0 else pre.next
        
