class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        ret = [];
        for i in range(left, right+1):
            isSelfDiv = True;
            for char in str(i):
                #print(int(char) == 0);
                if ((int(char) == 0) or (i % int(char) != 0)):
                    isSelfDiv = False;
                    break;
            if (isSelfDiv == True):
                ret.append(i);
        return ret;
        
