class Solution(object):
    def findLeastNumOfUniqueInts(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: int
        """
        count = collections.Counter(arr)
        freq = collections.defaultdict(list)
        for n, f in count.items():
            freq[f].append(n)
        
        for f in range(1, len(arr) + 1):
            if k == 0: break
            while freq[f] and f <= k:
                del count[freq[f].pop()]
                k -= f
        
        return len(count)
                
            
