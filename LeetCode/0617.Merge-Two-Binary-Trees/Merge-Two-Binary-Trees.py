# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if not t1: return t2
        queue = collections.deque()
        queue.append([t1, t2])
        while queue:
            n1, n2 = queue.popleft()
            #print(n1.val if n1 else 0, n2.val if n2 else 0)
            n1.val += n2.val if n2 else 0
                
            n1_left = n1.left if n1 else n1
            n2_left = n2.left if n2 else n2
            if not n1_left:
                n1.left = n2_left
            elif n2_left:
                queue.append([n1_left, n2_left])
            n1_right = n1.right if n1 else n1
            n2_right = n2.right if n2 else n2
            if not n1_right:
                n1.right = n2_right
            elif n2_right:
                queue.append([n1_right, n2_right])
        return t1
