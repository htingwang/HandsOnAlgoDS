# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        global idx
        idx = 0
        def helper(lower, upper):
            global idx
            if idx == len(preorder):
                return None
            val = preorder[idx]
            if val > upper or val < lower:
                return None
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root
        return helper(float('-inf'), float('inf'))
