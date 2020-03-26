# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        nodeA, nodeB = headA, headB;
        cycleA = cycleB = 0;
        while nodeA and nodeB:
            if nodeA == nodeB: return nodeA;
            nodeA, nodeB = nodeA.next, nodeB.next;
            if not cycleA and not nodeA: 
                nodeA = headB;
                cycleA = 1;
            if not cycleB and not nodeB: 
                nodeB = headA;
                cycleB = 1;
        return None;
