class Solution(object):
    def maxRepOpt1(self, text):
        """
        :type text: str
        :rtype: int
        """
        count = collections.Counter(text)
        i = 0
        A = []
        while i < len(text):
            j = i
            while j + 1 < len(text) and text[j + 1] == text[j]:      
                j += 1
            A.append([text[i], j - i + 1])
            i = j + 1

        res = max([min(l + 1, count[c]) for c, l in A])
        for i in range(1, len(A) - 1):
            if A[i - 1][0] == A[i + 1][0] and A[i][1] == 1:
                res = max(res, min(A[i - 1][1] + A[i + 1][1] + 1, count[A[i - 1][0]]))
        return res
