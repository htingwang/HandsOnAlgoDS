# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        self.helper(root)
        
    def helper(self, root):
        if not root:
            return [None, None]
        
        left_top, left_tail = self.helper(root.left)
        right_top, right_tail = self.helper(root.right)
        
        if left_top and right_top:
            root.right, left_tail.right = left_top, root.right
            root.left = None
            return [root, right_tail]
        if left_top:
            root.right = left_top
            root.left = None
            return [root, left_tail]
        if right_top:
            return [root, right_tail]
        return [root, root]
