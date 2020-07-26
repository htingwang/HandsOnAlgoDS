class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        m = {}
        for i in range(len(indices)):
            m[indices[i]] = s[i]
        res = []
        for i in range(len(indices)):
            res.append(m[i])
        return "".join(res)
        
