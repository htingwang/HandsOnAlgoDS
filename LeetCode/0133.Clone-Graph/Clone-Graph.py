"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node: return None
        clone = {}
        res = Node(node.val, [])
        clone[node] = res
        seen = set([node])
        queue = deque([node])
        
        while queue:
            cur = queue.popleft()
            #print cur.val
            for neighbor in cur.neighbors:
                if neighbor not in clone:
                    new = Node(neighbor.val, [])
                    clone[neighbor] = new
                clone[cur].neighbors.append(clone[neighbor])
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)
        
        return res
        
        
