class Solution(object):
    def primePalindrome(self, N):
        def is_prime(n):
            if n < 2: return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        def reverse(x):
            res = 0
            while x:
                res = 10 * res + x % 10
                x //= 10
            return res
        #print(is_prime(2), reverse(2))
        while True:
            if N == reverse(N) and is_prime(N):
                return N
            N += 1
            if 10 ** 7 < N < 10 ** 8:
                N = 10 ** 8
            if 10 ** 5 < N < 10 ** 6:
                N = 10 ** 6
            if 10 ** 3 < N < 10 ** 4:
                N = 10 ** 4   

