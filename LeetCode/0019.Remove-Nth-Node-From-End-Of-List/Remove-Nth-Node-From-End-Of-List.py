# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        length = 0
        first = head
        while first:
            length += 1
            first = first.next

        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next

        first.next = first.next.next
        return dummy.next

