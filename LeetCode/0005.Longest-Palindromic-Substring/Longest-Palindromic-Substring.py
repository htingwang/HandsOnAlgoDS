class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        def get_palindrome_length(s, left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return right - left - 1
        max_len = center = 0
        for i in range(len(s)):
            len1 = get_palindrome_length(s, i, i)
            len2 = get_palindrome_length(s, i, i + 1)
            if max(len1, len2) > max_len:
                max_len = max(len1, len2)
                center = i
        return s[center - (max_len - 1) // 2 : center + max_len // 2 + 1]
        
        
