class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root: return 0
        
        node = root
        depth = 0
        while node.left:
            node = node.left
            depth += 1
        
        if depth == 0: return 1
        
        left, right = 1, 2 ** depth - 1
        
        while left <= right:
            #print(left, right, depth)
            mid = left + (right - left) // 2
            if self.exist(root, mid, depth):
                left = mid + 1
            else:
                right = mid - 1
                
        return 2 ** depth - 1 + left
    
    def exist(self, node, value, depth):
        left, right = 0, 2 ** depth - 1
        for _ in range(depth):
            mid = left + (right - left) // 2
            if value <= mid:
                node = node.left
                right = mid
            else:
                node = node.right
                left = mid + 1
        return node is not None    
