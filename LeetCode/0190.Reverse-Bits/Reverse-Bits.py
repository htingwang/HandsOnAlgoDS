class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return self.reverseBits1(n)
    
    def reverseBits3(self, n):
        n = n >> 16 | n << 16
        n = (n & 0xff00ff00) >> 8 | (n & 0x00ff00ff) << 8
        n = (n & 0xf0f0f0f0) >> 4 | (n & 0x0f0f0f0f) << 4
        n = (n & 0xcccccccc) >> 2 | (n & 0x33333333) << 2
        n = (n & 0xaaaaaaaa) >> 1 | (n & 0x55555555) << 1
        return n
        
    def reverseBits2(self, n):
        res, power = 0, 24
        cache = {}
        while n:
            res += self.reverseByte(n & 0xff, cache) << power
            n >>= 8
            power -= 8
        return res
        
        
    def reverseBits1(self, n):
        res, power = 0, 31
        while n:
            res += (n & 1) << power
            n >>= 1
            power -= 1
        return res
        
    def reverseByte(self, byte, cache):
        if byte in cache: return cache[byte]
        cache[byte] = (byte * 0x0202020202 & 0x010884422010) % 1023 
        return cache[byte] 
