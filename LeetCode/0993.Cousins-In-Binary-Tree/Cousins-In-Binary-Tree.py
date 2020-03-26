# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        if not root: return False
        if root.val == x or root.val == y: return False
        
        queue = deque()
        queue.append((root, 0))
        memo = [-1, 0]
        while queue:
            node, level = queue.popleft()
            if node.right and node.left and set([node.left.val, node.right.val]) == set([x, y]):
                return False
            
            if node.val == x: memo[0] = level
            if node.val == y: memo[1] = level
            if memo[0] == memo[1]: return True
            if node.left:  queue.append((node.left, level + 1))
            if node.right: queue.append((node.right, level + 1))
        #print memo
        return False
