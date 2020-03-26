# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        global res
        if not root: return 0
        def helper(node):
            global res
            if not node:
                return (float('inf'), float('-inf'), 0)
            
            l_min, l_max, left_sz = helper(node.left)
            r_min, r_max, right_sz = helper(node.right)
            sz = left_sz + right_sz + 1

            if l_max < node.val and r_min > node.val:
                #print(node.val, l_min, l_max, r_min, r_max)
                res = max(res, sz)
                return (min(l_min, node.val), max(r_max, node.val), sz)
                
            return (float('-inf'), float('inf'), sz)
        res = 0
        helper(root)
        return res
