class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = [];
        for line in A:
            lineB = [];
            for i in range(len(line)):
                lineB.append(1-line[len(line)-1-i]);
            B.append(lineB);
        return B;
                
            
        
