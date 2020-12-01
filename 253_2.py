import heapq
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        size = len(intervals)
        if size == 1:
            return 1
        rooms = []
        intervals.sort(key = lambda x: (x[0], x[1]))
        heapq.heappush(rooms, intervals[0][1])
        for start, end in intervals[1:]:
            if rooms[0] <= start:
                heapq.heappop(rooms)
            heapq.heappush(rooms, end)
            
        answer = len(rooms)
        return answer
                
                
        
        
