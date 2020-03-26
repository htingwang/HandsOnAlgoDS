class Solution(object):
    def removeOuterParentheses(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = start = idx = 0;
        while (idx < len(S)):
            if S[idx] == "(": count += 1;
            if S[idx] == ")": count -= 1;
            if (count == 0):
                S = S[:start] + S[start+1:]
                S = S[:idx-1] + S[idx:]
                idx -= 2;
                start = idx + 1;
            idx += 1;
        return S;
