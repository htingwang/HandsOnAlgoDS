class Solution(object):
    def longestSubsequence(self, arr, difference):
        """
        :type arr: List[int]
        :type difference: int
        :rtype: int
        """
        num_to_idx = collections.defaultdict(list)
        num_to_idx[arr[0]].append(0)
        
        res = 1
        dp = [1] * (len(arr))
        for i in range(1, len(arr)):
            target = arr[i] - difference
            if target in num_to_idx:    
                dp[i] = dp[num_to_idx[target][-1]] + 1
                res = max(res, dp[i])
            num_to_idx[arr[i]].append(i)
        #print(prefix_sum)
        #print(dp)
        #print(num_to_idx)
        return res
            
            
       
        
        
