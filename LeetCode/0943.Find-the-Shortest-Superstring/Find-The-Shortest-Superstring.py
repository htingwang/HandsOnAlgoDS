class Solution(object):
    def shortestSuperstring(self, A):
        """
        :type A: List[str]
        :rtype: str
        """
        N = len(A)
        overlap = [[0] * N for _ in range(N)]
        
        for i, x in enumerate(A):
            for j, y in enumerate(A):
                if i != j:
                    for ans in range(min(len(x), len(y)), -1, -1):
                        if x.endswith(y[:ans]):
                            overlap[i][j] = ans
                            break
        
        dp = [[0] * N for _ in range(1 << N)]
        parent = [[None] * N for _ in range(1 << N)]
        
        for mask in range(1, 1 << N):
            for bit in range(N):
                if (mask >> bit) & 1:
                    pmask = mask ^ (1 << bit)
                    if pmask == 0: continue
                    for i in range(N):
                        if (pmask >> i) & 1:
                            cur = dp[pmask][i] + overlap[i][bit]
                            if cur > dp[mask][bit]:
                                dp[mask][bit] = cur
                                parent[mask][bit] = i

        last = max([(num, i) for i, num in enumerate(dp[-1])])[1]
        perm = []
        mask = (1 << N) - 1
        seen = set()
        while last != None:
            seen.add(last)
            perm.append(last)
            mask, last = mask ^ (1 << last), parent[mask][last]
        res = [A[perm[-1]]]

        for i in range(len(perm) - 2, -1, -1):
            word = A[perm[i]]
            cur_overlap = overlap[perm[i + 1]][perm[i]]
            res.append(word[cur_overlap:])

        for i in range(N):
            if i not in seen:
                res.append(A[i])
        return "".join(res)
