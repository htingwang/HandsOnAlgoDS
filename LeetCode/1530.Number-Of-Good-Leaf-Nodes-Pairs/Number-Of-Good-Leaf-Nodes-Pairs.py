# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def countPairs(self, root, distance):
        """
        :type root: TreeNode
        :type distance: int
        :rtype: int
        """
        return self.countPairs3(root, distance)
    
    def countPairs3(self, root, distance):
        self.res = 0
        
        def dfs(node, distance):
            m = collections.defaultdict(int) # depth: count
            if not node: return m
            if not node.left and not node.right: m[1] = 1
            left, right = dfs(node.left, distance), dfs(node.right, distance)
            for d1 in left:
                for d2 in right:
                    if d1 + d2 <= distance: 
                        self.res += left[d1] * right[d2]
                m[d1 + 1] = left[d1]
            for d2 in right: m[d2 + 1] += right[d2]
            return m
            
        dfs(root, distance)
        return self.res
        
    def countPairs2(self, root, distance):
        if not root: return 0
        queue = collections.deque([(root, 0, 1)])
        leaf = []
        while queue:
            cur, level, idx = queue.popleft()
            if cur.left:
                queue.append((cur.left, level + 1,  2 * idx))
            if cur.right:
                queue.append((cur.right, level + 1, 2 * idx + 1))
            if not cur.left and not cur.right:
                leaf.append((level, idx))
        def dist(n1, n2):
            #print(n1[1], n2[1])
            if n2[0] > n1[0]: n1, n2 = n2, n1
            l1, i1 = n1
            l2, i2 = n2
            res = 0
            while l1 > l2:
                i1 /= 2
                l1 -= 1
                res += 1
            while i1 != i2:
                i1 /= 2
                i2 /= 2
                res += 2
            return res
        res = 0
        for i in range(len(leaf)):
            for j in range(i + 1, len(leaf)):
                if dist(leaf[i], leaf[j]) <= distance: res += 1
        return res
            
    # Time limit exceeded  
    def countPairs1(self, root, distance):
        if not root: return 0
        #dp = [[0] * 101 for _ in range(101)]
        dp = collections.defaultdict(int)
        #seen = set([root])
        seen = set()
        queue = collections.deque([(root, None)])
        leaf = []
        while queue:
            cur, parent = queue.popleft()
            for node in seen:
                if node != parent:
                    #dp[cur.val][node.val] = dp[node.val][cur.val] = dp[cur.val][parent.val] + dp[parent.val][node.val]
                    dp[tuple([cur, node])] = dp[tuple([node, cur])] = dp[tuple([cur, parent])] + dp[tuple([parent, node])]
                    #print(cur.val, node.val, dp[cur.val][node.val], parent.val, dp[cur.val][parent.val], dp[parent.val][node.val])
            seen.add(cur)
            if cur.left:
                #dp[cur.val][cur.left.val] = dp[cur.left.val][cur.val] = 1
                dp[tuple([cur, cur.left])] = dp[tuple([cur.left, cur])] = 1
                #seen.add(cur.left)
                queue.append((cur.left, cur))
            if cur.right:
                #dp[cur.val][cur.right.val] = dp[cur.right.val][cur.val] = 1
                dp[tuple([cur, cur.right])] = dp[tuple([cur.right, cur])] = 1
                #seen.add(cur.right)
                queue.append((cur.right, cur))
            if not cur.left and not cur.right: leaf.append(cur)
        res = 0
        
        for i in range(len(leaf)):
            for j in range(i + 1, len(leaf)):
                #print(leaf[i], leaf[j], dp[leaf[i]][leaf[j]])
                #if dp[leaf[i]][leaf[j]] <= distance: res += 1
                if dp[tuple([leaf[i], leaf[j]])] <= distance: res += 1
        return res
            
                
        
