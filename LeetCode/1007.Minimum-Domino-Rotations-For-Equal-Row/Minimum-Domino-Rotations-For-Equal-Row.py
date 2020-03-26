class Solution(object):
    def minDominoRotations(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        res = [0] * 4
        n = len(A)
        target = A[0]
        for i in range(n):
            if A[i] != target:
                if B[i] == target:
                    res[0] += 1
                else:
                    res[0] = float('inf')
                    res[1] = float('inf')
                    break
            elif B[i] != target:
                res[1] += 1
                
        target = B[0]
        for i in range(n):
            if A[i] != target:
                if B[i] == target:
                    res[2] += 1
                else:
                    res[2] = float('inf')
                    res[3] = float('inf')
                    break
            elif B[i] != target:
                res[3] += 1
        return min(res) if min(res) != float('inf') else -1
