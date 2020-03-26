class Solution(object):
    def recoverTree(self, root):
        x = y = pre = None
        predecessor = None # Morris Traversal

        node = root
        while node:
            if node.left:
                predecessor = node.left
                while predecessor.right and predecessor.right != node:
                    predecessor = predecessor.right
                if predecessor.right:
                    if pre and node.val < pre.val:
                        y = node
                        if not x:
                            x = pre
                    pre = node
                    predecessor.right = None
                    node = node.right
                else:
                    predecessor.right = node
                    node = node.left
        
            else:
                if pre and node.val < pre.val:
                    y = node
                    if not x:
                        x = pre
                pre = node
                node = node.right
        x.val, y.val = y.val, x.val

