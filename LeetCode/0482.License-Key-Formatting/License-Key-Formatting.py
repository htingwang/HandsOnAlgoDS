class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        string = "".join(S.upper().split("-"))
        
        if K >= len(string):
            return string
        #print(string)
        res = string[: len(string) % K]
        
        for i in range(len(string) % K, len(string), K):
            res += "-" + string[i : i + K]
        #print(res)
        return res if res[0] != "-" else res[1:]
        
        
