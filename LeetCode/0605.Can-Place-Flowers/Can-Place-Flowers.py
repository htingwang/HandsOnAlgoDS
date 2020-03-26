class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        i = count = 0;
        while i < len(flowerbed):
            if (flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):
                flowerbed[i] = 1;
                count += 1;
            #print (count)
            if (n <= count):
                return True;
            i += 1;
        return False;
        
