class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        size = len(intervals)
        if size == 1:
            return 1
        times = {}
        intervals.sort(key = lambda x: (x[0], x[1]))
        for start, end in intervals:
            if start in times:
                times[start] += 1
            else:
                times[start] = 1
            if end in times:
                times[end] -= 1
            else:
                times[end] = -1
        answer = 0
        room = 0
        for time in sorted(times.keys()):
            room += times[time]
            if room > answer:
                answer = room
        return answer
                
                
        
        
