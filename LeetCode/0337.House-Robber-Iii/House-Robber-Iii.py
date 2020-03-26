# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return max(self.dfs(root))
    
    def dfs(self, node):
        if not node: return (0, 0)
        left = self.dfs(node.left)
        right = self.dfs(node.right)
        rob = node.val + left[1] + right[1]
        not_rob = max(left) + max(right)
        return (rob, not_rob)
