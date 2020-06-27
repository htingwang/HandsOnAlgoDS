class Solution(object):
    def maxJumps(self, arr, d):
        """
        :type arr: List[int]
        :type d: int
        :rtype: int
        """
        return self.maxJumps2(arr, d)
        
    # Monotone Stack + Dynamic programming. Time: O(N)
    def maxJumps2(self, arr, d):
        n = len(arr)
        stack = []
        dp = [1] * (n + 1)
        for i, h in enumerate(arr + [float('inf')]):
            while stack and arr[stack[-1]] < h:
                idxs = [stack.pop()]
                while stack and arr[stack[-1]] == arr[idxs[-1]]:
                    idxs.append(stack.pop())
                for j in idxs:
                    if i - j <= d:
                        dp[i] = max(dp[i], dp[j] + 1)
                    if stack and j - stack[-1] <= d:
                        dp[stack[-1]] = max(dp[stack[-1]], dp[j] + 1)   
            stack.append(i)
        
        return max(dp[: -1])
        
    # Dynamic programming. Time: O(Nd)
    def maxJumps1(self, arr, d):
        n = len(arr)
        h_idx = []
        for i, h in enumerate(arr): h_idx.append((h, i))
        h_idx.sort(reverse = True)    
        dp = [1] * n
        while h_idx:
            h, i = h_idx.pop()
            for ni in range(i - 1, i - d - 1, -1):
                if 0 <= ni < n:
                    if arr[ni] >= arr[i]: break
                    dp[i] = max(dp[i], dp[ni] + 1)
            for ni in range(i + 1, i + d + 1):
                if 0 <= ni < n:
                    if arr[ni] >= arr[i]: break
                    dp[i] = max(dp[i], dp[ni] + 1)
        return max(dp)
