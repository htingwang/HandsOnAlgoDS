class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        ans = [];
        val = 0;
        for x in A:
            val = val*2+x;
            if val % 5 == 0:
                ans.append(True);
            else:
                ans.append(False);
        return ans;
        
        
