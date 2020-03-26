# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sufficientSubset(self, root, limit):
        """
        :type root: TreeNode
        :type limit: int
        :rtype: TreeNode
        """
        def dfs(node, limit, pre):
            if not node: return pre
            left_val = dfs(node.left, limit, pre + node.val)
            right_val = dfs(node.right, limit, pre + node.val)
            if node.left and left_val < limit: node.left = None
            if node.right and right_val < limit: node.right = None
            return max(left_val, right_val)
        
        if dfs(root, limit, 0) < limit: return None
        return root
