# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        
        queue = collections.deque([(root, 1)])
        count = 0
        while queue:
            node, num = queue.popleft()
            count += 1
            if count != num:
                return False
            if node.left:
                queue.append((node.left, num * 2))
            if node.right:
                queue.append((node.right, num * 2 + 1))
        return True
