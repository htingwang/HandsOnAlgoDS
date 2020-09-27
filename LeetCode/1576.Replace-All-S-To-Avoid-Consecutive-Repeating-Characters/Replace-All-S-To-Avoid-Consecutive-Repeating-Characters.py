class Solution(object):
    def modifyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ['?'] + list(s) + ['?']
        n = len(s)
        for i in range(1, n + 1):
            c = res[i]
            if c == '?':
                if 'a' not in set([res[i - 1], res[i + 1]]):
                    res[i] = 'a'
                elif 'b' not in set([res[i - 1], res[i + 1]]):
                    res[i] = 'b'    
                else:
                    res[i] = 'c'
        
        return ''.join(res[1 : n + 1])
                
        
