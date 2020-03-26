# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return None
        queue = collections.deque([root])
        res = []
        while queue:
            n = len(queue)
            for i in range(n):
                cur = queue.popleft()
                if cur.left: queue.append(cur.left)
                if cur.right: queue.append(cur.right)
            res.append(cur.val)
        return res
        
