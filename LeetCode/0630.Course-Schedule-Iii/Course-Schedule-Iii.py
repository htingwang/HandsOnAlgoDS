class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key = lambda x: x[1])
        time = 0
        maxheap = []
        for c in courses:
            time += c[0]
            heapq.heappush(maxheap, -c[0])
            if time > c[1]:
                time += heapq.heappop(maxheap)
        return len(maxheap)
