class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        exists={};
        for c in A[0]:
            keys = exists.keys();
            if c in keys: exists[c] += 1;
            else: exists[c] = 1;
        keys = exists.keys();
        #print(sum(exists[i] for i in range(len(exitst[i])));
        for idx in range(1, len(A)):
            for key in keys:
                if (A[idx].count(key) < exists[key] ):
                    exists[key] = A[idx].count(key);
            
        ret = [];
        keys = exists.keys();
        for key in keys:
            for i in range(exists[key]):
                ret.append(key);
        return ret;
        
