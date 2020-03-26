# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head:
            return True
        if head.next is None:
            return True

        val_list = []
        while head:
            val_list.append(head.val)
            head = head.next

        mid_len = len(val_list) // 2
        is_even = len(val_list) % 2 == 0
        first_half_list = val_list[: mid_len][::-1]
        second_half_list = val_list[mid_len if is_even else mid_len + 1:]

        return first_half_list == second_half_list
