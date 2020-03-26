class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [];
        for j in range(len(A[0])):
            row = []
            for i in range(len(A)):   
                row.append(A[i][j])
            ret.append(row)
            #print ret
        return ret;
                
        
