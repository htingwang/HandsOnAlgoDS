"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        
        next_node = None
        if root.next:
            node = root.next
            while node:
                if node.left:
                    next_node = node.left
                    #print(cur.val, node.left.val)
                    break
                if node.right:
                    next_node = node.right
                    #print(cur.val, node.right.val)
                    break
                node = node.next
        if root.left:
            root.left.next = root.right if root.right else next_node
        if root.right:
            root.right.next = next_node
        
            #print(root.left.val, root.right.val)
        #self.connect(root.left)
        self.connect(root.right)
        self.connect(root.left)
        #self.connect(root.right)
        return root
