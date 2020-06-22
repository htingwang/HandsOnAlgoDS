class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        
        return self.avoidFlood2(rains)
    
    # Heap. Time: O(nlogn)
    def avoidFlood2(self, rains):
        n = len(rains)
        res = [1] * n
        lake_to_idx = collections.defaultdict(collections.deque)
        for i, lake in enumerate(rains):
            lake_to_idx[lake].append(i)
            
        closest = []
        seen = set()
        
        for i, lake in enumerate(rains):
            if lake == 0:
                if closest:
                    res[i] = rains[heapq.heappop(closest)]
                    seen.remove(res[i])
            else:
                if lake in seen: return []
                lake_to_idx[lake].popleft()
                if lake_to_idx[lake]:
                    heapq.heappush(closest, lake_to_idx[lake][0])
                seen.add(lake)
                res[i] = -1
                
        return res        
        
    # Binary search. Time: O(n＾2). If using treeset in other language, time: O(nlogn)
    def avoidFlood1(self, rains):
        n = len(rains)
        res = [1] * n
        dry = []
        seen = {}
        for i, lake in enumerate(rains):
            if lake == 0:
                dry.append(i)
            else:
                if lake in seen:
                    j = bisect.bisect_left(dry, seen[lake])
                    if j == len(dry): return []
                    res[dry[j]] = lake
                    dry.remove(dry[j])
                res[i] = -1
                seen[lake] = i
        return res
        
