class Solution(object):
    def findAllConcatenatedWordsInADict(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        if len(words) <= 1: return []
        
        words_set = set(words)
        res = []
        
        for word in words:
            n = len(word)
            if n == 0: continue
            dp = [False] * (n + 1)
            dp[0] = True
            for i in range(n + 1):
                if not dp[i]: continue
                if i > 0 and word[i : n] in words_set:
                    res.append(word)
                    break
                for j in range(i + 1, n + 1):
                    if j - i < n and word[i : j] in words_set:
                        dp[j] = True
                if dp[n]:
                    res.append(word)
                    break
        return res
