# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def dfs(node):
            if not node: return -1
            d = 1 + max(dfs(node.left), dfs(node.right))
            if d >= len(res): res.append([])
            res[d].append(node.val)
            return d
        dfs(root)
        return res
