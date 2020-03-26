class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        i = 0
        while i < len(data):
            n = 0
            if data[i] >> 7  == 0:
                n = 1
            if data[i] >> 5 == 0b110:
                n = 2
            if data[i] >> 4 == 0b1110:
                n = 3
            if data[i] >> 3 == 0b11110:
                n = 4
            if n == 0: return False
            i += 1
            #print n, i,data[i] // 64
            while n > 1:
                if i >= len(data) or data[i] >> 6 != 0b10:
                    return False
                n -= 1
                i += 1
        return True
                
