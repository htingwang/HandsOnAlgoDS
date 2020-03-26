from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = prefix_sums = 0
        length = len(nums)
        hash_map = defaultdict(int)
        hash_map[0] = 1
        for i in range(length):
            prefix_sums += nums[i]  # get the accumulate sub set.
            # this is very important, this is find #_of_occurrence_of_the_prefixSum_value in the hash_map.
            count += hash_map[prefix_sums - k]
            # increase 1 for prefixSum_vale in the hash_map.
            hash_map[prefix_sums] += 1
        return count
            
