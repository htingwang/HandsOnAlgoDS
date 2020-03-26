# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = ""
        if not root: return res
        
        queue = collections.deque([root])
        
        while queue:
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node: 
                    res += str(node.val) + ","
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    res += "null,"
        #print(res.strip(","))
        return res.strip(",")

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        data_list = data.split(",")
        
        #print(data_list)
        
        root = TreeNode(int(data_list[0]))
        queue = collections.deque([root])
        i = 1
        while i < len(data_list):
            node = queue.popleft()
            if i < len(data_list) and data_list[i] != "null":
                node.left = TreeNode(int(data_list[i]))
                queue.append(node.left)
            if i + 1 < len(data_list) and data_list[i + 1] != "null":
                node.right = TreeNode(int(data_list[i + 1]))
                queue.append(node.right)
            i += 2
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
