"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
       
        node = head
        while node:
            new = Node(node.val, None, None)
            new.next = node.next
            node.next = new
            node = new.next
            
        node = head
        while node:
            #print(node.val)
            new = node.next
            next_node = new.next
            if node.random: new.random = node.random.next
            node = next_node
            
            
        node = head
        ret = head.next
        while node:
            #print(node.val)
            new = node.next
            next_node = new.next
            if next_node: new.next = next_node.next
            node.next = next_node
            node = next_node
        return ret

        
