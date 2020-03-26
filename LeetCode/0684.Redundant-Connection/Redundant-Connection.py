class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        def find(x):
            while x != f[x]:
                x = f[x]
                f[x] = f[f[x]]
            return x
        n = len(edges)
        f = [i for i in range(n + 1)]
        for u, v in edges:
            u_root, v_root = find(u), find(v)
            if u_root == v_root:
                return [u, v]
            f[u_root] = v_root
            
        return []
