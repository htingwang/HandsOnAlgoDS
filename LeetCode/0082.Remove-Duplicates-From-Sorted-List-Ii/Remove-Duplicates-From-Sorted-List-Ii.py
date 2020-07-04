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
        return self.deleteDuplicates2(head)
    
    def deleteDuplicates2(self, head):
        if not head: return head
        if head.next and head.next.val == head.val:
            while head.next and head.next.val == head.val:
                head = head.next
            return self.deleteDuplicates2(head.next)
        head.next = self.deleteDuplicates2(head.next)
        return head
            
        
    def deleteDuplicates1(self, head):
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        while pre.next:
            cur = pre.next
            while cur.next and cur.next.val == cur.val:
                cur = cur.next
            if cur != pre.next: pre.next = cur.next
            else: pre = pre.next
        
        return dummy.next
