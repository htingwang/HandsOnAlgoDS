"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        return self.flatten1(head)
    
    def flatten2(self, head):
        if not head: return head
        dummy = Node(0, None, head, None)
        prev = dummy
        stack = [head]
        while stack:
            cur = stack.pop()
            cur.prev = prev
            prev.next = cur
            if cur.next:
                stack.append(cur.next)
            if cur.child:
                stack.append(cur.child)
                cur.child = None
            prev = cur
        
        head.prev = None
        return head
    
    def flatten1(self, head): 
        if not head: return head
        dummy = Node(0, None, head, None)
        self.dfs(dummy, head)
        head.prev = None
        return head
    
    def dfs(self, prev, cur):
        if not cur: return prev
        next_node = cur.next
        cur.prev = prev
        prev.next = cur
        tail = self.dfs(cur, cur.child)
        cur.child = None
        return self.dfs(tail, next_node)
        
