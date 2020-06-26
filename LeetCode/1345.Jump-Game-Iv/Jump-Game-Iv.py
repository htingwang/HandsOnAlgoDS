class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """

        num_idx = collections.defaultdict(list)
        for i, num in enumerate(arr): num_idx[num].append(i)
            
        queue = collections.deque([(0, 0)])
        seen = set([0])
        while queue:
            
            cost, i = queue.popleft()
            if i == len(arr) - 1: return cost
            for ni in [i - 1, i + 1] + num_idx[arr[i]]:
                if ni == i: continue
                if 0 <= ni < len(arr) and ni not in seen:
                    queue.append((cost + 1, ni))
                    seen.add(ni)
            del num_idx[arr[i]]      
        return -1
            
        
