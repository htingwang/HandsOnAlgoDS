class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        i, j = 0, 1
        if len(s) <= 1: return len(s)
        count = set(s[i])
        ans = 0
        while j < len(s):
            if s[j] in count:
                while i < j:
                    if s[i] == s[j]:
                        i += 1
                        break;
                    count.remove(s[i])
                    i += 1
            ans = max(ans, j - i + 1)
            count.add(s[j])
            j += 1
        return ans
