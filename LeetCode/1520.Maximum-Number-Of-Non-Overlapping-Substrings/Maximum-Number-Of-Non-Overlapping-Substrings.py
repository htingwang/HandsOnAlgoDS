class Solution(object):
    def maxNumOfSubstrings(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        l, r = {}, {}
        for i, c in enumerate(s):
            if c not in l: l[c] = r[c] = i
            l[c] = min(l[c], i)
            r[c] = max(r[c], i)
            
        def get_left(right):
            left, i = l[s[right]], right
            while i >= left:
                if r[s[i]] > right: return -1
                left = min(left, l[s[i]])
                i -= 1
            return left
        
        res = []
        left = 0
        for right, c in enumerate(s):
            if right < left: continue
            if r[c] == right:
                c_left = get_left(right)
                if c_left >= left:
                    res.append(s[c_left : right + 1])
                    left = max(left, right + 1)
        return res
