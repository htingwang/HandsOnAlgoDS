# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        return self.closestValue2(root, target)
    
    def closestValue2(self, root, target):
        res = root.val
        node = root
        while node:
            if abs(node.val - target) <= abs(res - target):
                res = node.val
            node = node.left if target < node.val else node.right
        return res
            
        
    def closestValue1(self, root, target):
        res, diff = None, float('inf')
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            cur = stack.pop()
            if abs(cur.val - target) < diff:
                diff = abs(cur.val - target)
                res = cur.val
            else:
                break
            node = cur.right
        return res
