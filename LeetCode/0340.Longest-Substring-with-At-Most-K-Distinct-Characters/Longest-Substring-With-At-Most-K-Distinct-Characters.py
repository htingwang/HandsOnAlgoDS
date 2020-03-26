class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n = len(s)
        i = j = 0
        ans = 0
        count = [0] * 256
        cnt = 0
        for i in range(n):
            while j < n:
                count[ord(s[j]) - ord("a")] += 1
                if count[ord(s[j]) - ord("a")] == 1:
                    cnt += 1
                if cnt <= k:
                    #print i, j
                    ans = max(ans, j - i + 1)
                j += 1
                if cnt > k: break
            count[ord(s[i]) - ord("a")] -= 1
            if count[ord(s[i]) - ord("a")] == 0:
                cnt -= 1
        return ans
                
