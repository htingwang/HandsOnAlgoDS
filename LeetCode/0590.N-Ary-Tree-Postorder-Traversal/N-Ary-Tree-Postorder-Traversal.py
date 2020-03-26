"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def postorder(self, root):
        """
        :type root: Node
        :rtype: List[int]
        """
        if (not root): return [];
        if (not root.children): return [root.val];
        ret = []
        for child in root.children:
            ret += (self.postorder(child));
        ret.append(root.val);
        return ret;
