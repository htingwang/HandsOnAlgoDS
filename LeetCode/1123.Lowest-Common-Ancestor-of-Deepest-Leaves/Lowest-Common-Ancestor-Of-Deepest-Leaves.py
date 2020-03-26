# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        d, ancestor = self.dfs(root)
        return ancestor
    
    def dfs(self, node):
        if not node: return (0, None)
        d1, a1 = self.dfs(node.left)
        d2, a2 = self.dfs(node.right)
        if d1 > d2: 
            return d1 + 1, a1
        if d2 > d1:
            return d2 + 1, a2
        return d1 + 1, node
        
            
        
