class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        return self.getSkyline2(buildings)
    
    # Using Priority queue. Time: O(NlogN). Space: O(N)
    def getSkyline2(self, buildings):
        res = []
        b = []
        for i, (s, e, h) in enumerate(buildings):
            b.append((s, -h, i))
            b.append((e, h, i))
        b.sort()
        maxheap = [(0, -1)]
        rmset = set()
        pre = cur = 0
        for p, h, i in b:
            if h < 0: heapq.heappush(maxheap, (h, i))
            else:
                rmset.add((-h, i))
            while maxheap[0] in rmset:
                rmset.remove(maxheap[0])
                heapq.heappop(maxheap)
            cur = -maxheap[0][0]
            if pre != cur:
                res.append([p, cur])
                pre = cur
        return res
        
    # Using MyHeapHash. Time: O(NlogN). Space: O(N)
    def getSkyline1(self, buildings):
        res = []
        b = []
        for i, (s, e, h) in enumerate(buildings):
            b.append((s, -h, i))
            b.append((e, h, i))
        b.sort()
        maxheap = MyHeapHash()
        maxheap.push((0, -1))
        pre = cur = 0
        for p, h, i in b:
            if h < 0: maxheap.push((h, i))
            else: maxheap.remove((-h, i))
            cur = -maxheap.top()[0]
            if cur != pre:
                res.append([p, cur])
                pre = cur
        return res
    
class MyHeapHash(object):
    def __init__(self):
        self.heap =[]
        self.hash = {}
        self.size = 0
    
    def top(self):
        return self.heap[0]
    
    def push(self, val):
        self.heap.append(val)
        self.hash[val] = len(self.heap) - 1
        self.size += 1
        self.sift_up(self.hash[val])
        
    def remove(self, val):
        if val not in self.hash: return
        
        idx = self.hash[val]
        self.heap[idx], self.heap[-1] = self.heap[-1], self.heap[idx]
        self.hash[self.heap[idx]] = idx
        
        self.heap.pop()
        del self.hash[val]
        self.size -= 1
        
        if idx < self.size:
            self.sift_up(idx)
            self.sift_down(idx)
        
    def pop(self):
        val = self.heap[0]
        self.remove(val)
        return val
    
    def sift_up(self, idx):
        while (idx - 1) // 2 >= 0:
            if self.heap[idx] >= self.heap[(idx - 1) // 2]: break
            self.heap[idx], self.heap[(idx - 1) // 2] = self.heap[(idx - 1) // 2], self.heap[idx]
            self.hash[self.heap[idx]] = idx
            self.hash[self.heap[(idx - 1) // 2]] = (idx - 1) // 2
            idx = (idx - 1) // 2
            
    def sift_down(self, idx):
        while 2 * idx + 1 < self.size:
            l = r = 2 * idx + 1
            if l < self.size - 1: r += 1
            if self.heap[idx] <= min(self.heap[l], self.heap[r]): break
            target = l
            if self.heap[r] < self.heap[l]: target = r
            self.heap[idx], self.heap[target] = self.heap[target], self.heap[idx]
            self.hash[self.heap[idx]] = idx
            self.hash[self.heap[target]] = target
            idx = target
        
