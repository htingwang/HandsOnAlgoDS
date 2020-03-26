import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])
        free_room = []
        heapq.heappush(free_room, intervals[0][1])

        for interval in intervals[1:]:
            if free_room[0] <= interval[0]:
                heapq.heappop(free_room)

            heapq.heappush(free_room, interval[1])

        return len(free_room)
