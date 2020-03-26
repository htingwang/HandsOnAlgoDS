# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def predecessor(root):
            root = root.left
            while root.right:
                root = root.right
            return root.val
        def successor(root):
            root = root.right
            while root.left:
                root = root.left
            return root.val
        
        if not root: return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left and not root.right:
                root = None
            elif root.right:
                val = successor(root)
                root.val = val
                root.right = self.deleteNode(root.right, val)
            else:
                val = predecessor(root)
                root.val = val
                root.left = self.deleteNode(root.left, val)
        return root
        
