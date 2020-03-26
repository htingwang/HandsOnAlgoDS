class Solution(object):
    def numKLenSubstrNoRepeats(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: int
        """
        count = {}
        ans = left = cnt = 0
        for i, c in enumerate(S):
            count[c] = count.get(c, 0) + 1
            if count[c] == 1:
                cnt += 1
            if i >= K - 1:
                if cnt == K:
                    ans += 1
                count[S[i - K + 1]] -= 1
                if count[S[i - K + 1]] == 0:
                    cnt -= 1
        return ans
        
