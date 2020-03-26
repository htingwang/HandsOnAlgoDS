class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        max_value = int(math.pow(2, 31)) - 1
        min_value = -int(math.pow(2, 31))
        is_negative = ((dividend > 0) == (divisor < 0))
        if divisor == 0:
            return max_value
        if divisor == 1:
            if is_negative:
                return max(min_value, dividend)
            else:
                # make sure the Maximum is not out of scope [-2 ** 31, 2 ** 31 - 1]
                return min(max_value, dividend)
        if divisor == -1:
            if is_negative:
                return -min(-min_value, dividend)
            else:
                return min(max_value, abs(dividend))

        divisor = abs(divisor)
        dividend = abs(dividend)
        deno_count = 0
        while dividend >= divisor:
            count, dividend = self.divideWhile(dividend, divisor)
            deno_count += count

        return -deno_count if is_negative else abs(deno_count)

    def divideWhile(self, dividend, divisor):
        res, count = 0, 1
        while dividend >= divisor:
            dividend -= divisor
            divisor += divisor

            res += count
            count += count
        return res, dividend
