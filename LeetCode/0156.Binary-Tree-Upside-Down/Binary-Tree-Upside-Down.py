# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.upsideDownBinaryTree2(root)
        
    def upsideDownBinaryTree2(self, root):
        if not root or not root.left: return root
        l, r = root.left, root.right
        res = self.upsideDownBinaryTree2(l)
        l.left = r
        l.right = root
        root.left = root.right = None
        return res
        
    def upsideDownBinaryTree1(self, root):
        cur, pre, pre_right = root, None, None
        while cur:
            n_node = cur.left
            cur.left = pre_right
            pre_right = cur.right
            cur.right = pre
            pre = cur
            cur = n_node
        return pre
        
