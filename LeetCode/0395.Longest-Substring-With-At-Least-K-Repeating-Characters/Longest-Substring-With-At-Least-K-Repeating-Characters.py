class Solution(object):
    def longestSubstring(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        res = 0
        n = len(s)
        for cnt in range(1, 27): #cnt distinct characters
            left = right = 0
            unique_count = 0
            char_count = collections.defaultdict(int)
            for right in range(n):
                valid = True
                if char_count[s[right]] == 0: unique_count += 1
                char_count[s[right]] += 1
                while unique_count > cnt:
                    if char_count[s[left]] == 1: unique_count -= 1
                    char_count[s[left]] -= 1
                    left += 1
                for c in char_count:
                    if 0 < char_count[c] < k:
                        valid = False
                        break
                #print(cnt, left, right, char_count)
                if valid:
                    res = max(res, right - left + 1)
        return res

