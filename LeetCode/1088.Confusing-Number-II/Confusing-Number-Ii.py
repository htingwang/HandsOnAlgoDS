class Solution(object):
    def confusingNumberII(self, N):
        """
        :type N: int
        :rtype: int
        """
        mapping = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        options = ["0", "1", "6", "8", "9"]
        candidates = [""]
        digit = len(str(N))
        for _ in range(min(digit, 9)):
            candidates = [j + i for j in candidates for i in options]

        res = 0
        if N == 10 ** 9: res += 1
        for num_str in candidates:
            if int(num_str) > N: break
            if self.check(num_str, mapping): res += 1
        return res
    
    def check(self, num_str, mapping):
        num_str = num_str.lstrip("0")
        left, right = 0, len(num_str) - 1
        while left < right:
            if mapping[num_str[left]] != num_str[right]: return True
            left += 1
            right -= 1
        if left == right and (num_str[left] == "6" or num_str[right] == "9"):
            return True
        return False
