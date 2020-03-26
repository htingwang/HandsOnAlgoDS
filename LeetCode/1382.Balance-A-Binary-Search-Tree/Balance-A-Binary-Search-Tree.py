# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def balanceBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        nodes = []
        node = root
        queue = []
        while node or queue:
            while node:
                queue.append(node)
                node = node.left
            node = queue.pop()
            nodes.append(node)
            node = node.right
        return self.build_tree(nodes, 0, len(nodes) - 1)
        
    def build_tree(self, nodes, start, end):
        if start > end: return None
        mid = (start + end) // 2
        root = nodes[mid]
        root.left = self.build_tree(nodes, start, mid - 1)
        root.right = self.build_tree(nodes, mid + 1, end)
        return root
            
        
