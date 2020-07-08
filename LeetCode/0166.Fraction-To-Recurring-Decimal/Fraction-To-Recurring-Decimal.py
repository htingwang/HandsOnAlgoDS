class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        sign = 1
        if (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0): sign = -1
        rem_pos = {}
        ans = abs(numerator) // abs(denominator)
        rem = abs(numerator) % abs(denominator)
        res = str(ans)
        if sign == -1 and (ans != 0 or rem != 0): res = '-' + res
        if rem == 0: return res
        res += "."
        s = ""
        pos = 0

        while rem:
            if rem in rem_pos:
                s = s[: rem_pos[rem]] + '(' + s[rem_pos[rem]:] + ')'
                break
            rem_pos[rem] = pos
            pos += 1
            s += str((rem * 10) // abs(denominator))
            rem = (rem * 10) % abs(denominator)

        return res + s
