# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        def check_node(p, q):
            if not p: return not q
            if not q: return not p
            return p.val == q.val
        
        queue = collections.deque()
        queue.append((p, q))
        while queue:
            n1, n2 = queue.popleft()
            if check_node(n1, n2) == False:
                return False
            if n1: 
                queue.append((n1.left, n2.left))
                queue.append((n1.right, n2.right))
        return True
        
