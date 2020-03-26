class Solution(object):
    def longestRepeatingSubstring(self, S):
        """
        :type S: str
        :rtype: int
        """
        n = len(S)
        if n <= 1: return 0
        
        left, right = 1, n
        while left <= right:
            mid = (left + right) // 2
            if self.search(S, mid, n) == -1:
                right = mid - 1
            else:
                left = mid + 1
        return left - 1
            
    def search(self, S, L, n):
        mod = 2 ** 31 - 1
        seen = set()
        
        power = 1
        for i in range(L - 1):
            power = (power * 31) % mod
            
        hashcode = 0
        for i in range(n):
            hashcode = (hashcode * 31 + ord(S[i])) % mod
            if i >= L - 1:
                if hashcode in seen:
                    return i
                seen.add(hashcode)
                hashcode = (hashcode - power * ord(S[i - L + 1])) % mod
                
        return -1
