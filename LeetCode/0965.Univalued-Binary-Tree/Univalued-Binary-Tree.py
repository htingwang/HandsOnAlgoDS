# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        nodeleft = (not root.left or (root.val == root.left.val and self.isUnivalTree(root.left)));
        noderight = (not root.right or (root.val == root.right.val and self.isUnivalTree(root.right)));
        return (nodeleft and noderight);
        
