# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root: return 0

        return self.dfs(root, 0, sum) + self.pathSum(root.left, sum) + self.pathSum(root.right, sum)
    
    def dfs(self, root, pre, sum):
        if not root: return 0
        cur = pre + root.val
        return (cur == sum) + self.dfs(root.left, cur, sum) + self.dfs(root.right, cur, sum)
        
