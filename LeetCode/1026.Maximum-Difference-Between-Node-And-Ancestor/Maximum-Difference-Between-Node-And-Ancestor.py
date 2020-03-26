# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.helper(root, root.val, root.val);
    
    def helper(self, root, vmin, vmax):
        if (not root): return (vmax - vmin);
        vmin = min(vmin, root.val);
        vmax = max(vmax, root.val);
        return max(self.helper(root.left, vmin, vmax), self.helper(root.right, vmin, vmax));
        
