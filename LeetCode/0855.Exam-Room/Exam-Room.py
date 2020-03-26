class ExamRoom(object):

    def __init__(self, N):
        """
        :type N: int
        """
        self.maxheap = [(-self.dist(-1, N), -1, N)]
        self.N = N

    def seat(self):
        """
        :rtype: int
        """
        d, left, right = heapq.heappop(self.maxheap)
        d = -d
        if left == -1:
            student = 0
        elif left == self.N:
            student = self.N - 1
        else:
            student = left + d
        heapq.heappush(self.maxheap, (-self.dist(left, student), left, student))
        heapq.heappush(self.maxheap, (-self.dist(student, right), student, right))
        return student
        

    def leave(self, p):
        """
        :type p: int
        :rtype: None
        """
        remove = []
        start = end = 0
        for i in range(len(self.maxheap)):
            d, left, right = self.maxheap[i]
            if left == p: 
                end = right
                remove.append((d, left, right))
            if right == p: 
                start = left
                remove.append((d, left, right))
        self.maxheap.remove(remove[0])
        self.maxheap.remove(remove[1])
        self.maxheap.append((-self.dist(start, end), start, end))
        heapq.heapify(self.maxheap)
        
    def dist(self, left, right):
        if left == -1 or right == self.N:
            return right - left - 1
        return (right - left) // 2
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)
