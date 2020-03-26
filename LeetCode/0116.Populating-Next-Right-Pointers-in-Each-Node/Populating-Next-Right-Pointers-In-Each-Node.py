"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if root and root.left and root.right:
            root.left.next = root.right
            root.right.next = root.next.left if root.next else None
            self.connect(root.left)
            self.connect(root.right)
        return root
            
        
        
