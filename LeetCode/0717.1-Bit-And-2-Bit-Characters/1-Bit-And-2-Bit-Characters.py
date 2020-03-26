class Solution(object):
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        idx = 0;
        while (idx < len(bits)-1):           
            if (bits[idx] == 0): 
                idx += 1;
            else: 
                idx += 2;
        if (idx == len(bits)-1): return True;
        return False;
            
            
        
