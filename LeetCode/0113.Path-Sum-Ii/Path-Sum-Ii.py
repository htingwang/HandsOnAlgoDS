# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        cur = []
        res = []
        def dfs(root, sum, cur, res):
            if not root: return
                
            cur.append(root.val)
            
            if not root.left and not root.right and root.val == sum:
                res.append(cur[:])
            else:
                dfs(root.left, sum - root.val, cur, res)
                dfs(root.right, sum - root.val, cur, res)
            cur.pop()
            
        dfs(root, sum, cur, res)
        
        return res
        
