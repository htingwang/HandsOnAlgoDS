from collections import defaultdict
from collections import deque
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n - 1 != len(edges): return False
        
        father = [-1] * n
        
        for u, v in edges:
            x = self.find(father, u)
            y = self.find(father, v)
            if x == y: return False
            father[x] = y
            
        return True
            
    def find(self, father, node):
        while father[node] != -1:
            node = father[node]
        return node
