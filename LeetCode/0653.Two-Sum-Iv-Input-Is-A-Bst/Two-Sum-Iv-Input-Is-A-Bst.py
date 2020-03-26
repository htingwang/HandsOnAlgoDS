# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        inorder = []
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            inorder.append(node.val)
            node = node.right
        #print(inorder)
        left, right = 0, len(inorder) - 1
        while left < right:
            cur = inorder[left] + inorder[right]
            if cur == k:
                return True
            if cur < k:
                left += 1
            else:
                right -= 1
        return False
                
