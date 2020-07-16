# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node):
            if not node: return (True, 0)
            isleft, left = dfs(node.left)
            isright, right = dfs(node.right)
            if isleft and (not node.left or node.left.val == node.val) and isright and (not node.right or node.right.val == node.val):
                return (True, left + right + 1)
            return (False, left + right)
        
        return dfs(root)[1]
