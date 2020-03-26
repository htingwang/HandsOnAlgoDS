# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return head;
        node, i, ret = head, 0, None;
        while node:
            node = node.next;
            i += 1;
        link_len = i;
        if k % link_len == 0: return head;
        node, i, ret = head, 0, None;
        while node:
            tmp_node = node.next;
            if tmp_node == None:
                node.next = head;
                break;
            if i == link_len - k % link_len - 1:             
                node.next = None;
                ret = tmp_node;
            node = tmp_node;
            i += 1;
        return ret;
        
