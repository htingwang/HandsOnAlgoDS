class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        for start, end, interval in [(0, len(s), 1), (len(s) - 1, -1, -1)]:
            left = right = 0
            for i in range(start, end, interval):
                if s[i] == "(":
                    left += 1
                else:
                    right += 1
                if left == right:
                    res = max(res, right * 2)
                if (start == 0 and right) > left or (start == len(s) - 1 and left > right):
                    left = right = 0
        return res
