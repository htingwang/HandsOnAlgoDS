# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        res = []
        if root.left or root.right: res.append(root.val)
            
        node = root.left
        while node:
            if node.left or node.right: res.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
                
        stack = [root]
        while stack:
            node = stack.pop()
            if not node.left and not node.right:
                res.append(node.val)
            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)
                
        right = []
        node = root.right
        while node:
            if node.left or node.right: right = [node.val] + right
            if node.right:
                node = node.right
            else:
                node = node.left
        return res + right
