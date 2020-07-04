# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def dfs(s, e):
            if s > e: return [None]
            res = []
            for i in range(s, e + 1):
                left = dfs(s, i - 1)
                right = dfs(i + 1, e)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        return dfs(1, n) if n else []

