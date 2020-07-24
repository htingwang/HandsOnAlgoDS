class Solution(object):
    def breakPalindrome(self, palindrome):
        """
        :type palindrome: str
        :rtype: str
        """
        res = list(palindrome)
        for i in range(len(res) // 2):
            if res[i] != 'a': 
                res[i] = 'a'
                return "".join(res)
        res[-1] = 'b'
        return "" if len(res) < 2 else "".join(res)
