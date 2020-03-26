# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ##### slow fast pointer needs only space O(1) ####
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
        
        ###### hashmap need space O(N)####
        map_table = {}
        i = 0
        node = head
        while node:
            map_table[i] = node
            node = node.next
            i += 1

        return map_table[i / 2]
