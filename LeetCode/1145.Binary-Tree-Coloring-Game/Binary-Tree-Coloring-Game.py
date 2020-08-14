# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def btreeGameWinningMove(self, root, n, x):
        """
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        children = [0, 0]
        def count(node):
            if not node: return 0
            l, r = count(node.left), count(node.right)
            if node.val == x:
                children[0], children[1] = l, r
            return l + r + 1
        n = count(root)
        return max(max(children), n - sum(children) - 1) > n / 2

        
