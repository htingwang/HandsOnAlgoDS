# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        def helper(node):
            if not node: return ""
            return helper(node.left) + "," + helper(node.right) + "," + str(node.val)
            
        res = helper(root)
        print(res)
        return res

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        def helper(lower, upper):
            if not values or values[-1] < lower or values[-1] > upper:
                return None
            val = values.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root
        
        values = [int(x) for x in data.strip().split(",") if x]
        return helper(float('-inf'), float('inf'))
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
