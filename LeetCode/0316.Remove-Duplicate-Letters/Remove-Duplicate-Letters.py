class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        counter = [0] * 26 #collections.Counter(s)
        for c in s:
            counter[ord(c) - ord("a")] += 1
        ans = ""
        visit = [0] * 26
        for c in s:
            counter[ord(c) - ord("a")] -= 1

            if visit[ord(c) - ord("a")] == 0:
                while len(ans) > 0 and ord(c) < ord(ans[-1]) and counter[ord(ans[-1]) - ord("a")] > 0:
                    visit[ord(ans[-1]) - ord("a")] = 0
                    ans = ans[:-1]

                ans += c
                visit[ord(c) - ord("a")] = 1
                
        return ans
        
