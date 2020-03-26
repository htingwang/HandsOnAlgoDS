# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        self.res = 0
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        if not node: return 0
        
        l, r = self.dfs(node.left), self.dfs(node.right)
        
        depth = max(l, r) + 1
        self.res = max(self.res, l + r)
        
        return depth
