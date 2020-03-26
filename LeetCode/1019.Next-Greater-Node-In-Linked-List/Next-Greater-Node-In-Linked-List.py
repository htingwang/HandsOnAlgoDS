# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        stack = []
        node = head
        while node:
            while stack and stack[-1][1].val < node.val:
                cur = stack.pop()
                res[cur[0]] = node.val   
            stack.append([len(res), node])
            res.append(0)
            node = node.next
        return res
