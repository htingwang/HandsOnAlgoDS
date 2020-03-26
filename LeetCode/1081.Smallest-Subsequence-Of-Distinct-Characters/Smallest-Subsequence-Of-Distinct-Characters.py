class Solution(object):
    def smallestSubsequence(self, text):
        """
        :type text: str
        :rtype: str
        """
        ans = ""
        counter = [0] * 26
        for c in text:
            counter[ord(c) - ord("a")] += 1
        visit = [0] * 26
        for c in text:
            counter[ord(c) - ord("a")] -= 1
            if not visit[ord(c) - ord("a")]:
                while len(ans) > 0 and ord(c) < ord(ans[-1]) and counter[ord(ans[-1]) - ord("a")] > 0:
                    visit[ord(ans[-1]) - ord("a")] = 0
                    ans = ans[:-1]
                ans += c
                visit[ord(c) - ord("a")] = 1
        return ans
