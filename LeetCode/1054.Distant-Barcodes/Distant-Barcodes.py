class Solution(object):
    def rearrangeBarcodes(self, barcodes):
        """
        :type barcodes: List[int]
        :rtype: List[int]
        """
        count = collections.Counter(barcodes)
        maxheap = []
        for key in count:
            heapq.heappush(maxheap, (-count[key], key))
        
        i = 0
        while i < len(barcodes):
            cnt1, val1 = heapq.heappop(maxheap)
            barcodes[i] = val1
            i += 1
            if i < len(barcodes):
                cnt2, val2 = heapq.heappop(maxheap)
                barcodes[i] = val2
                i += 1
                heapq.heappush(maxheap, (cnt2 + 1, val2))
            heapq.heappush(maxheap, (cnt1 + 1, val1))
            
        return barcodes
        
