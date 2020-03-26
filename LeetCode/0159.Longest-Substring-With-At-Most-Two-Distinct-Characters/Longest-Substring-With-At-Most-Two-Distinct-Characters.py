class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = [0] * 256
        cnt = i = j = ans = 0
        for i in range(len(s)):
            while j < len(s):
                count[ord(s[j]) - ord("a")] += 1
                if count[ord(s[j]) - ord("a")] == 1:
                    cnt += 1
                if cnt <= 2:
                    ans = max(ans, j - i + 1)
                j += 1
                if cnt > 2: break
            count[ord(s[i]) - ord("a")] -= 1
            if count[ord(s[i]) - ord("a")] == 0:
                cnt -= 1
        return ans
        
