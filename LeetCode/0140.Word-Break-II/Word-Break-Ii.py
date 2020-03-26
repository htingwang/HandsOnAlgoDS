from collections import deque, defaultdict
class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        if not wordDict:
            return []
        n = len(s)
        dp = [[] for _ in range(n + 1)]
        dp[0].append(-1)
        wordSet = set(wordDict)
        max_len = max(len(word) for word in wordDict)
        for i in range(1, n + 1):
            for j in range(1, min(i, max_len) + 1):
                if dp[i - j] and s[i - j : i] in wordSet:
                    dp[i].append(i - j)       
        #print(dp)
        queue = deque()
        queue.append(n)
        ans_dict = defaultdict(set)
        ans_dict[n] = [""]

        while queue:
            cur = queue.popleft()
            for i in dp[cur]:
                if i < 0 : break
                for word in ans_dict[cur]:
                    if word == "": ans_dict[i].add(s[i:cur])
                    else: ans_dict[i].add(s[i:cur] + " " + word)
                queue.append(i)

        return ans_dict[0]
