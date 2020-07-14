# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        return self.lowestCommonAncestor2(root, p, q)
    
    def lowestCommonAncestor2(self, root, p, q):
        node = root
        while node:
            if p.val < node.val and q.val < node.val:
                node = node.left
            elif p.val > node.val and q.val > node.val:
                node = node.right
            else: return node
        return None
        
    def lowestCommonAncestor1(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor1(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor1(root.right, p, q)
        else: return root
