# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        
        queue = collections.deque([root])
        res = []
        
        level = 0
        while queue:
            n = len(queue)
            cur = []
            for i in range(n):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                cur.append(node.val)
            if level % 2 == 0:
                res.append(cur)
            else:
                res.append(cur[:: - 1])
            level += 1
        return res
