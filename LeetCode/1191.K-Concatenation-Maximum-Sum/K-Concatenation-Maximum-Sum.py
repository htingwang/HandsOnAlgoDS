class Solution(object):
    def kConcatenationMaxSum(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        s = [0] * (len(arr) + 1)
        left_min = 0
        max_sub_sum = float('-inf')
        for i in range(1, len(arr) + 1):
            s[i] = s[i - 1] + arr[i - 1]
            max_sub_sum = max(max_sub_sum, s[i] - left_min)
            left_min = min(left_min, s[i])
        if k == 1:
            return max_sub_sum if max_sub_sum > 0 else 0
        #print(s)    
        arr_sum = s[len(arr)]
        arr_max = max(s)
        arr_min = min(s)
        #print(arr_sum, arr_max, arr_min,max_sub_sum, arr_max + 1 * arr_sum - arr_min)
        #print(arr_max + (k - 1) * arr_sum - arr_min)
        res = max_sub_sum
        for i in range(1, k):
            #print(arr_max + i * arr_sum - arr_min)
            res = max(res, arr_max + i * arr_sum - arr_min)
        if res < 0: return 0
        return res % (10 ** 9 + 7)
        #return max(0, (arr_max + (k - 1) * arr_sum - arr_min) % (10 ** 9 + 7))

        
