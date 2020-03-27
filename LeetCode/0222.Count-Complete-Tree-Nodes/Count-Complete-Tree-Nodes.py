# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.countNodes2(root)
    
    def countNodes2(self, root):
        if not root: return 0
        d = 0
        node = root
        while node.left:
            d += 1
            node = node.left
        left, right = 0, 2 ** d - 1
        while left < right:
            mid = (left + right + 1) // 2
            if self.exist(root, d, mid):
                left = mid
            else:
                right = mid - 1
        return 2 ** d + left
    
    def exist(self, node, d, idx):
        left, right = 0, 2 ** d - 1
        for _ in range(d):
            mid = (left + right) // 2
            if mid >= idx:
                right = mid
                node = node.left
            else:
                left = mid + 1
                node = node.right
        return node != None
                
    def countNodes1(self, root):
        return self.countNodes(root.left) + self.countNodes(root.right) + 1 if root else 0
