class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        if not wordDict: return not s
        n = len(s)
        word_set = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        max_len = max([len(w) for w in wordDict])
        for i in range(1, n + 1):
            for j in range(1, min(i, max_len) + 1):
                if dp[i - j] and s[i - j: i] in word_set:
                    dp[i] = True
                    break
        return dp[n]
        
