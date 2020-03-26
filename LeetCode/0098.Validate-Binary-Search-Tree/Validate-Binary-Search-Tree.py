# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def rightLargeLeftChecker(node, lower=float('-inf'), upper=float('inf')):
            if node is None:
                return True

            val = node.val
            if val <= lower or val >= upper:
                return False

            if not rightLargeLeftChecker(node.right, val, upper):
                return False

            if not rightLargeLeftChecker(node.left, lower, val):
                return False

            return True

        return rightLargeLeftChecker(root)
