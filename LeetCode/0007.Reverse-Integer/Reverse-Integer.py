class Solution:
    def reverse(self, x: int) -> int:
        reversed = int("".join(list(str(abs(x)))[::-1]))
        if x < 0:
            return max(-reversed, -2**31) if max(-reversed, -2**31) > -2**31 else 0
        return min(reversed, 2**31 - 1) if min(reversed, 2**31 - 1) < 2**31 - 1 else 0
