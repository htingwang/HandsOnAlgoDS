class HeapHash(object):
    def __init__(self):
        self.hash = {}
        self.heap = []
    
    def size(self):
        return len(self.heap)
    
    def push(self, num):
        self.heap.append(num)
        self.hash[num] = self.size() - 1
        self.sift_up(self.size() - 1)
        
    def top(self):
        return self.heap[0]
    
    def pop(self):
        num = self.heap[0]
        self.remove(num)
        return num
    
    def remove(self, num):
        if num not in self.hash:
            return
        
        idx = self.hash[num]
        self.swap(idx, self.size() - 1)
        
        self.heap.pop()
        del self.hash[num]
        
        if idx == self.size():
            return
        
        self.sift_up(idx)
        self.sift_down(idx)
        
    def sift_up(self, idx):
        while (idx - 1) // 2 >= 0:
            parent = (idx - 1) // 2
            if self.heap[parent] <= self.heap[idx]:
                break
            self.swap(idx, parent)
            idx = parent
            
    def sift_down(self, idx):
        while idx * 2 + 1 < self.size():
            left, right = idx * 2 + 1, idx * 2 + 2
            smallest = idx
            if self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < self.size() and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == idx:
                break
            self.swap(idx, smallest)
            idx = smallest
        
    def swap(self, idx1, idx2):
        num1, num2 = self.heap[idx1], self.heap[idx2]
        self.heap[idx1], self.heap[idx2] = num2, num1
        self.hash[num1], self.hash[num2] = idx2, idx1
        
class Solution(object):
    def medianSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[float]
        """ 
        minheap = HeapHash()
        maxheap = HeapHash()
        res = []
        
        for i, num in enumerate(nums):
            minheap.push((num, i))
            cur, idx = minheap.pop()
            maxheap.push((-cur, idx))
            while minheap.size() < maxheap.size():
                cur, idx = maxheap.pop()
                minheap.push((-cur, idx))
            if i >= k - 1:
                median = minheap.top()[0]
                if minheap.size() == maxheap.size():
                    median = (minheap.top()[0] - maxheap.top()[0]) / 2.0
                res.append(median)
                minheap.remove((nums[i - k + 1], i - k + 1))
                maxheap.remove((-nums[i - k + 1], i - k + 1))
        return res
