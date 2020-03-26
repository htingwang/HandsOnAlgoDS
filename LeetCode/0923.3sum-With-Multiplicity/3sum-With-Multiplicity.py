class Solution:
    def threeSumMulti(self, A: List[int], target: int) -> int:
        MOD = 10**9 + 7
        ans = 0
        counter = collections.Counter(A)
        for i in range(101):
            for j in range(i, 101):
                k = target - i - j
                if k > 100 or k < 0: continue
                if i == j == k:
                    ans += (counter[i]) * (counter[i] - 1) * (counter[i] - 2) // 6
                elif i == j != k:
                    ans += counter[k] * counter[i] * (counter[i] - 1) // 2
                elif k > j:
                    ans += counter[i] * counter[j] * counter[k]
        return ans%MOD
