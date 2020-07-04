# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder: return None
        
        toidx = {val: i for i, val in enumerate(inorder)}
        n = len(inorder)
        def dfs(inorder, s, e, postorder):
            if s > e: return None

            val = postorder.pop()
            root = TreeNode(val)
            
            root.right = dfs(inorder, toidx[val] + 1, e, postorder)
            root.left = dfs(inorder, s, toidx[val] - 1, postorder)
            
            return root
        
        return dfs(inorder, 0, n - 1, postorder)
        
