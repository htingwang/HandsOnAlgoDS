class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        #if not k: return k in nums
        prefix_sum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefix_sum[i + 1] = prefix_sum[i] + nums[i]
            
        prefix_to_idx = collections.defaultdict(list)
        mod = k if k else float('inf')
        for i in range(len(nums) + 1):
            check = (prefix_sum[i] - k) % mod
            #print(i, check, prefix_sum,prefix_to_idx)
            if  check in prefix_to_idx and i - prefix_to_idx[check][0] > 1:
                #print(i, prefix_sum[i], seen)
                return True
            prefix_to_idx[prefix_sum[i] % mod].append(i)
            
        return False
