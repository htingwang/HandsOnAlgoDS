# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.res = -sys.maxsize - 1
        self.dfs(root)
        return self.res
    
    def dfs(self, node):
        if not node: return 0
        
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        
        p_sum  = node.val
        if left > 0: p_sum += left
        if right > 0: p_sum += right
        self.res = max(self.res, p_sum)
        
        d_sum = node.val
        if max(left, right) > 0: d_sum += max(left, right)
        return d_sum
        
        
