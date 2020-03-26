class Solution(object):
    def myPow(self, x, n, m):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if n == 0: return 1;
        if n == -1: return 1/x;
        tmp = self.myPow(x, n//2, m);
        if n % 2 == 0:
            return (tmp * tmp) % m;
        else:
            return (x * tmp * tmp) % m; 
        
    def superPow(self, a, b):
        """
        :type a: int
        :type b: List[int]
        :rtype: int
        """
        power = int(''.join(map(str, b)));
        return self.myPow(a, power, 1337) % 1337
