class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        len_t = len(trust)
        if len_t < N - 1: return -1
        candidates = [0] * (N + 1)
        for i, j in trust:
            candidates[i] -= 1
            candidates[j] += 1
        #print(candidates)
        for i in range(1, len(candidates)):
            if candidates[i] == N - 1:
                return i
        return -1
        
        
