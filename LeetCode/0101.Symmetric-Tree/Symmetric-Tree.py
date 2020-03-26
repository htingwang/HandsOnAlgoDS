# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(node1: TreeNode, node2: TreeNode):
            if node1 == node2 is None:
                return True
            if node1 is None or node2 is None:
                return False

            return all(((node1.val == node2.val),
                       isMirror(node1.left, node2.right),
                       isMirror(node1.right, node2.left)))
        return isMirror(root, root)
