class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        left = right = 0
        res = 0
        for c in S:
            if c == "(":
                left += 1
            else:
                if left:
                    left -= 1
                else:
                    right += 1
        #print(left, right)
        return left + right
