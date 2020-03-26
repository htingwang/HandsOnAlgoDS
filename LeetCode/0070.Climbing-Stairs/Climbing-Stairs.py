class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return n
        a, b = 1, 2
        for i in range(3, n + 1):
            sums = a + b
            a = b
            b = sums
        return b
