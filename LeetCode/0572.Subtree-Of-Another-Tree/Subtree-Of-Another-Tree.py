# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        def equal(s, t): 
            if not s and not t: return True
            if not s or not t: return False
            if s.val != t.val: return False
            #print(s.val, t.val)
            return equal(s.left, t.left) and equal(s.right, t.right)
            
        def traverse(s, t):
            if not s: return False
            return equal(s, t) or traverse(s.left, t) or traverse(s.right, t)
        
        return traverse(s, t)
