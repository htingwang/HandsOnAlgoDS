# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = 1
        
        def dfs(node, length):
            if node.left:
                if node.left.val == node.val + 1: dfs(node.left, length + 1)
                else: dfs(node.left, 1)
                 
            if node.right:
                if node.right.val == node.val + 1: dfs(node.right, length + 1)
                else: dfs(node.right, 1)
            self.res = max(self.res, length)
            
        dfs(root, 1)
        return self.res
