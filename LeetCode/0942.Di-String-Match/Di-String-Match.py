class Solution(object):
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        lo, hi = 0, len(S);
        output = [];
        for s in S:
            if (s == "I"):
                output.append(lo);
                lo += 1;
            else:
                output.append(hi);
                hi -= 1;
        output.append(hi);
        return output;
            
        # [0,1,2,3] "III"
        # [0,1,3,2] "IID"
        # [0,2,1,3] "IDI"
        # [0,2,3,1] "IID"
        # [0,3,1,2] "IDI"
        # [0,3,2,1] "DDD"
        # [1,0,2,3] "DII"
        # [1,0,3,2] "DID"
        # [1,2,0,3] "IDI"
        # [0,1,2] "II"
        # [0,2,1] "ID"
        # [1,0,2] "DI"
        # [1,2,0] "ID"
        # [2,0,1] "DI"
        # [2,1,0] "DD"
        
