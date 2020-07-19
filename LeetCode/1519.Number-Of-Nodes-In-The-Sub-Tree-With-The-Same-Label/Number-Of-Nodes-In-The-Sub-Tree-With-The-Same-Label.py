class Solution(object):
    def countSubTrees(self, n, edges, labels):
        """
        :type n: int
        :type edges: List[List[int]]
        :type labels: str
        :rtype: List[int]
        """
        res = [0] * n
        tree = collections.defaultdict(set)
        for u, v in edges:
            tree[u].add(v)
            tree[v].add(u)
        seen = set()

        def dfs(node):
            seen.add(node)
            count = collections.defaultdict(int)
            for c in tree[node]:
                if c not in seen:
                    scount = dfs(c)
                    for key in scount:
                        count[key] += scount[key]
            count[labels[node]] += 1
            res[node] = count[labels[node]]
            return count
        
        dfs(0)
        return res
        
