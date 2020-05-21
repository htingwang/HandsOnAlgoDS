class Solution():
    def multiply(self, A, B):
        Arows = collections.defaultdict(list)
        m, n, nB = len(A), len(A[0]), len(B[0])
        res = [[0] * nB for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    Arows[i].append((j, A[i][j]))
        for i in range(m):
            for col, val in Arows[i]:
                for j in range(nB):
                    res[i][j] += val * B[col][j]
        return res

